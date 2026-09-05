# Scripts de Utilidad

## generate_avatar.py

Pipeline por API (sin ComfyUI local) para generar videos de avatar IA hablando un guion:

1. **ElevenLabs** — texto a voz (`audio.mp3`)
2. **Replicate (Flux.1) o Fal.ai** — imagen hiperrealista del avatar
3. **Replicate (SadTalker) o Hedra Character-3** — anima boca/cara sincronizada con el audio
4. **faster-whisper + ffmpeg** — transcribe y quema subtítulos automáticos (100% local, gratis)

> Nota: LivePortrait transfiere movimiento desde un video guía, no anima desde audio.
> Para lip-sync audio-driven se usa SadTalker (default, vía Replicate) o Hedra Character-3.

Instalación:
```bash
pip install -r requirements-avatar.txt
# ffmpeg debe estar instalado en el sistema (apt install ffmpeg / brew install ffmpeg)
cp .env.avatar.example .env  # completa tus API keys y haz `source .env`
```

Uso:
```bash
python generate_avatar.py --script "Hola, este es el nuevo producto de e-commerce..." \
    --voice-id 21m00Tcm4TlvDq8ikWAM --subtitles --out output/
```

Argumentos principales:
- `--script` / `--script-file`: guion a narrar (uno de los dos, requerido)
- `--voice-id`: Voice ID de ElevenLabs (default: voz de ejemplo "Rachel")
- `--avatar-prompt` / `--avatar-image`: prompt para generar el avatar, o ruta a una imagen ya lista
- `--image-provider {replicate,fal}` (default: replicate)
- `--animator {sadtalker,hedra}` (default: sadtalker)
- `--subtitles`: genera y quema subtítulos automáticos
- `--out`: carpeta de salida (default: `output/`)

Variables de entorno (según proveedores usados): `ELEVENLABS_API_KEY`, `REPLICATE_API_TOKEN`, `FAL_KEY`, `HEDRA_API_KEY`.

Salida: `output/final.mp4` (o `avatar_raw.mp4` si no se usa `--subtitles`).

## comfyui_run.py

Script Python minimalista para encolar y ejecutar workflows de ComfyUI via HTTP API.
Responsabilidad única: encola el workflow y hace polling hasta completar.
No modifica el JSON - toda la edición debe hacerse antes de llamar al script.

Uso:
~/ComfyUI/venv/bin/python comfyui_run.py --workflow path/to/workflow.json

Argumentos:
- --workflow (requerido): Ruta al JSON en formato API
- --host (default: 127.0.0.1): Host del servidor ComfyUI
- --port (default: 8188): Puerto del servidor
- --timeout (default: 300): Segundos máximos de espera
- --poll (default: 1.5): Segundos entre polls al historial

Salida (stdout JSON):
{ "prompt_id": "...", "images": [{ "filename": "out.png", "subfolder": "", "type": "output" }] }

Ruta de imágenes: ComfyUI/output/<subfolder>/<filename>

Fuente: https://github.com/kelvincai522/comfyui-skill

## install-comfyui-linux.sh (pendiente)

Script de instalación automática en Linux con venv.

## install-custom-nodes.sh (pendiente)

Clona los nodos personalizados más populares automáticamente.

## launch-flags.md (pendiente)

Documentación de todos los flags de lanzamiento de ComfyUI.
