#!/usr/bin/env python3
"""Pipeline de generación de video avatar IA: guion -> voz -> imagen -> animación -> subtítulos.

Orquesta servicios externos por API (sin usar ComfyUI local):
  1. ElevenLabs      -> texto a voz (audio .mp3)
  2. Replicate/Fal   -> imagen hiperrealista de avatar (Flux.1)
  3. Replicate/Hedra -> animación de rostro/labios sincronizada con el audio
  4. faster-whisper + ffmpeg -> subtítulos automáticos quemados en el video

Nota técnica: LivePortrait transfiere movimiento desde un VIDEO guía, no genera
lip-sync a partir de audio. Para animar boca/cara desde un audio se usa un modelo
"talking head" (por defecto SadTalker via Replicate) o el servicio Hedra
Character-3 (audio-nativo, mejor calidad, requiere cuenta/API key propia).

Uso:
    python generate_avatar.py --script "Hola, este es el nuevo producto..." \\
        --voice-id 21m00Tcm4TlvDq8ikWAM --out output/

    python generate_avatar.py --script-file guion.txt --animator hedra --subtitles

Variables de entorno requeridas (según los proveedores usados):
    ELEVENLABS_API_KEY   siempre
    REPLICATE_API_TOKEN  si --image-provider replicate (default) o --animator sadtalker (default)
    FAL_KEY              si --image-provider fal
    HEDRA_API_KEY        si --animator hedra
"""
from __future__ import annotations

import argparse
import os
import sys
import time
import json
import textwrap
import subprocess
from pathlib import Path
from urllib.parse import urlparse

import requests

ELEVENLABS_API_URL = "https://api.elevenlabs.io/v1"
HEDRA_API_URL = "https://api.hedra.com/web-app/public"
DEFAULT_VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # "Rachel", voz de ejemplo de ElevenLabs
DEFAULT_FLUX_MODEL = "black-forest-labs/flux-1.1-pro"
DEFAULT_SADTALKER_MODEL = "lucataco/sadtalker:a519cc0cfebaaeade068b23899165a11ec76aaa1d2b313d5e1c2e10d5d0e6f43"


class PipelineError(RuntimeError):
    """Error irrecuperable de un paso del pipeline."""


def require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise PipelineError(
            f"Falta la variable de entorno {name}. Expórtala antes de correr el script."
        )
    return value


def download(url: str, dest: Path, timeout: int = 120) -> Path:
    resp = requests.get(url, timeout=timeout, stream=True)
    resp.raise_for_status()
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "wb") as fh:
        for chunk in resp.iter_content(chunk_size=1 << 16):
            fh.write(chunk)
    return dest


# --------------------------------------------------------------------------
# 1. Texto -> audio (ElevenLabs)
# --------------------------------------------------------------------------
def generate_audio(text: str, voice_id: str, out_path: Path, model_id: str = "eleven_multilingual_v2") -> Path:
    api_key = require_env("ELEVENLABS_API_KEY")
    url = f"{ELEVENLABS_API_URL}/text-to-speech/{voice_id}"
    headers = {"xi-api-key": api_key, "Content-Type": "application/json", "Accept": "audio/mpeg"}
    payload = {
        "text": text,
        "model_id": model_id,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
    }
    resp = requests.post(url, headers=headers, json=payload, timeout=120)
    if not resp.ok:
        raise PipelineError(f"ElevenLabs TTS falló ({resp.status_code}): {resp.text[:500]}")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(resp.content)
    return out_path


# --------------------------------------------------------------------------
# 2. Prompt -> imagen de avatar (Flux.1 via Replicate o Fal.ai)
# --------------------------------------------------------------------------
def generate_avatar_image_replicate(prompt: str, out_path: Path, model: str = DEFAULT_FLUX_MODEL) -> Path:
    require_env("REPLICATE_API_TOKEN")
    try:
        import replicate
    except ImportError as exc:
        raise PipelineError("Falta el paquete 'replicate'. Instala con: pip install replicate") from exc

    output = replicate.run(
        model,
        input={
            "prompt": prompt,
            "aspect_ratio": "9:16",
            "output_format": "png",
        },
    )
    url = output[0] if isinstance(output, list) else output
    url = getattr(url, "url", url)  # replicate>=0.30 devuelve FileOutput
    return download(str(url), out_path)


def generate_avatar_image_fal(prompt: str, out_path: Path, model: str = "fal-ai/flux/dev") -> Path:
    require_env("FAL_KEY")
    try:
        import fal_client
    except ImportError as exc:
        raise PipelineError("Falta el paquete 'fal-client'. Instala con: pip install fal-client") from exc

    result = fal_client.subscribe(
        model,
        arguments={"prompt": prompt, "image_size": "portrait_16_9"},
    )
    url = result["images"][0]["url"]
    return download(url, out_path)


# --------------------------------------------------------------------------
# 3. Imagen + audio -> video animado (SadTalker via Replicate, o Hedra)
# --------------------------------------------------------------------------
def animate_sadtalker(image_path: Path, audio_path: Path, out_path: Path, model: str = DEFAULT_SADTALKER_MODEL) -> Path:
    require_env("REPLICATE_API_TOKEN")
    try:
        import replicate
    except ImportError as exc:
        raise PipelineError("Falta el paquete 'replicate'. Instala con: pip install replicate") from exc

    with open(image_path, "rb") as img_fh, open(audio_path, "rb") as audio_fh:
        output = replicate.run(
            model,
            input={
                "source_image": img_fh,
                "driven_audio": audio_fh,
                "still": True,
                "preprocess": "full",
                "enhancer": "gfpgan",
            },
        )
    url = getattr(output, "url", output)
    return download(str(url), out_path)


def animate_hedra(image_path: Path, audio_path: Path, out_path: Path, aspect_ratio: str = "9:16") -> Path:
    api_key = require_env("HEDRA_API_KEY")
    headers = {"X-API-KEY": api_key}

    def upload_asset(path: Path, asset_type: str) -> str:
        create = requests.post(
            f"{HEDRA_API_URL}/assets",
            headers=headers,
            json={"name": path.name, "type": asset_type},
            timeout=60,
        )
        if not create.ok:
            raise PipelineError(f"Hedra: no se pudo crear el asset {asset_type} ({create.status_code}): {create.text[:300]}")
        asset_id = create.json()["id"]
        with open(path, "rb") as fh:
            upload = requests.post(
                f"{HEDRA_API_URL}/assets/{asset_id}/upload",
                headers=headers,
                files={"file": fh},
                timeout=120,
            )
        if not upload.ok:
            raise PipelineError(f"Hedra: falló la subida del asset {asset_id} ({upload.status_code}): {upload.text[:300]}")
        return asset_id

    image_asset_id = upload_asset(image_path, "image")
    audio_asset_id = upload_asset(audio_path, "audio")

    gen = requests.post(
        f"{HEDRA_API_URL}/generations",
        headers=headers,
        json={
            "type": "video",
            "ai_model_id": "character-3",
            "start_keyframe_id": image_asset_id,
            "audio_id": audio_asset_id,
            "aspect_ratio": aspect_ratio,
        },
        timeout=60,
    )
    if not gen.ok:
        raise PipelineError(f"Hedra: no se pudo iniciar la generación ({gen.status_code}): {gen.text[:300]}")
    generation_id = gen.json()["id"]

    poll_url = f"{HEDRA_API_URL}/generations/{generation_id}/status"
    deadline = time.time() + 900
    while time.time() < deadline:
        status_resp = requests.get(poll_url, headers=headers, timeout=30)
        status_resp.raise_for_status()
        data = status_resp.json()
        status = data.get("status")
        if status == "complete":
            video_url = data["url"]
            return download(video_url, out_path)
        if status in ("error", "failed"):
            raise PipelineError(f"Hedra: la generación falló: {data}")
        time.sleep(5)
    raise PipelineError("Hedra: timeout esperando la generación del video (15 min)")


# --------------------------------------------------------------------------
# 4. Subtítulos automáticos (faster-whisper) quemados con ffmpeg
# --------------------------------------------------------------------------
def transcribe_to_srt(audio_path: Path, srt_path: Path, model_size: str = "base") -> Path:
    try:
        from faster_whisper import WhisperModel
    except ImportError as exc:
        raise PipelineError(
            "Falta el paquete 'faster-whisper'. Instala con: pip install faster-whisper"
        ) from exc

    model = WhisperModel(model_size, compute_type="int8")
    segments, _info = model.transcribe(str(audio_path))

    def fmt_ts(seconds: float) -> str:
        ms = int(round(seconds * 1000))
        h, ms = divmod(ms, 3_600_000)
        m, ms = divmod(ms, 60_000)
        s, ms = divmod(ms, 1000)
        return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

    lines = []
    for i, seg in enumerate(segments, start=1):
        lines.append(str(i))
        lines.append(f"{fmt_ts(seg.start)} --> {fmt_ts(seg.end)}")
        lines.append(seg.text.strip())
        lines.append("")

    srt_path.parent.mkdir(parents=True, exist_ok=True)
    srt_path.write_text("\n".join(lines), encoding="utf-8")
    return srt_path


def burn_subtitles(video_path: Path, srt_path: Path, out_path: Path) -> Path:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    srt_escaped = str(srt_path).replace("\\", "/").replace(":", "\\:")
    cmd = [
        "ffmpeg", "-y",
        "-i", str(video_path),
        "-vf", f"subtitles='{srt_escaped}':force_style='FontSize=18,Outline=1,BorderStyle=3'",
        "-c:a", "copy",
        str(out_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise PipelineError(f"ffmpeg falló quemando subtítulos:\n{result.stderr[-2000:]}")
    return out_path


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Genera un video de avatar IA (voz + imagen + animación + subtítulos) desde un guion.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(__doc__ or ""),
    )
    script_group = parser.add_mutually_exclusive_group(required=True)
    script_group.add_argument("--script", help="Texto del guion a narrar")
    script_group.add_argument("--script-file", type=Path, help="Archivo .txt con el guion")

    parser.add_argument("--out", type=Path, default=Path("output"), help="Carpeta de salida (default: output/)")
    parser.add_argument("--voice-id", default=DEFAULT_VOICE_ID, help="Voice ID de ElevenLabs")
    parser.add_argument(
        "--avatar-prompt",
        default="retrato hiperrealista de una persona profesional mirando a cámara, estudio, luz suave",
        help="Prompt para generar la imagen del avatar (se ignora si se usa --avatar-image)",
    )
    parser.add_argument("--avatar-image", type=Path, help="Ruta a una imagen de avatar ya existente (omite la generación)")
    parser.add_argument("--image-provider", choices=["replicate", "fal"], default="replicate")
    parser.add_argument("--animator", choices=["sadtalker", "hedra"], default="sadtalker")
    parser.add_argument("--subtitles", action="store_true", help="Genera y quema subtítulos automáticos")
    parser.add_argument("--whisper-model", default="base", help="Tamaño del modelo faster-whisper (default: base)")
    parser.add_argument("--keep-intermediate", action="store_true", help="No borra archivos intermedios")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    script_text = args.script if args.script else args.script_file.read_text(encoding="utf-8")
    if not script_text.strip():
        parser.error("El guion está vacío")

    out_dir = args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        print("[1/4] Generando audio con ElevenLabs...")
        audio_path = generate_audio(script_text, args.voice_id, out_dir / "audio.mp3")
        print(f"      -> {audio_path}")

        if args.avatar_image:
            image_path = args.avatar_image
            print(f"[2/4] Usando imagen de avatar existente: {image_path}")
        else:
            print(f"[2/4] Generando imagen de avatar ({args.image_provider})...")
            image_path = out_dir / "avatar.png"
            if args.image_provider == "replicate":
                generate_avatar_image_replicate(args.avatar_prompt, image_path)
            else:
                generate_avatar_image_fal(args.avatar_prompt, image_path)
            print(f"      -> {image_path}")

        print(f"[3/4] Animando avatar ({args.animator})...")
        raw_video_path = out_dir / "avatar_raw.mp4"
        if args.animator == "sadtalker":
            animate_sadtalker(image_path, audio_path, raw_video_path)
        else:
            animate_hedra(image_path, audio_path, raw_video_path)
        print(f"      -> {raw_video_path}")

        final_video_path = raw_video_path
        if args.subtitles:
            print("[4/4] Transcribiendo audio y quemando subtítulos...")
            srt_path = transcribe_to_srt(audio_path, out_dir / "subtitles.srt", args.whisper_model)
            final_video_path = out_dir / "final.mp4"
            burn_subtitles(raw_video_path, srt_path, final_video_path)
            print(f"      -> {final_video_path}")
        else:
            print("[4/4] Subtítulos omitidos (usa --subtitles para activarlos)")

        if not args.keep_intermediate and final_video_path != raw_video_path:
            raw_video_path.unlink(missing_ok=True)

        print(f"\nVideo final: {final_video_path.resolve()}")
        return 0

    except PipelineError as exc:
        print(f"\nERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
