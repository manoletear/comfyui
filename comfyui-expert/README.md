# ComfyUI-Expert (VideoAgent)

Repositorio: https://github.com/MCKRUZ/ComfyUI-Expert

Orquestador de sesión basado en Claude Code que convierte a Claude en un
director técnico senior de producción de video con IA. Enruta peticiones en
lenguaje natural a 12 módulos de skills especializados que cubren el pipeline
completo de producción de video con ComfyUI.

## Inicio Rápido

git clone https://github.com/MCKRUZ/ComfyUI-Expert.git
cd ComfyUI-Expert
video-agent.bat

Opciones:
video-agent.bat --project "mi-video"
video-agent.bat --comfyui "http://ip-remota:8188"
video-agent.bat --resume

## Los 12 Skills

### Fundación
- comfyui-api: Conexión REST API, polling cada 5s, gestión VRAM
- comfyui-inventory: Descubrimiento de modelos y nodos, cache en inventory.json
- project-manager: Estado del proyecto, perfiles de personajes, historial

### Investigación
- comfyui-research: Monitorea 7 canales YT, 11 repos GitHub, HuggingFace trending

### Creación
- comfyui-prompt-engineer: Optimización por modelo (FLUX, SDXL, SD1.5, Wan)
- comfyui-workflow-builder: Genera workflow JSON desde lenguaje natural

### Producción
- comfyui-video-pipeline: Wan 2.2 / FramePack / AnimateDiff
- comfyui-voice-pipeline: TTS (6 herramientas) + lip-sync (4 métodos)
- comfyui-lora-training: Dataset prep + training FLUX/SDXL

### Salida
- video-assembly: FFmpeg + Remotion, normalización -16 LUFS
- video-publisher: Metadata YouTube + upload delegation

### Soporte
- comfyui-troubleshooter: Diagnóstico de 4 categorías, top 10 errores

## Sistema de 3 Tiers

Tier 1 - Fundación: foundation/*.md, ~2K tokens, cargado al inicio de sesión
Tier 2 - Trabajo: projects/{name}/*, cuando se trabaja en un proyecto específico
Tier 3 - Referencia: references/*.md, solo cuando un skill lo necesita

## Casos de Uso

"Genera un retrato fotorrealista de Sage usando InstantID"
"Haz que Sage diga Bienvenidos a mi canal"
"Entrena un LoRA con estas 20 imágenes"
"Revisa nuevos modelos de ComfyUI este mes"

## Compatibilidad OpenClaw

La carpeta openclaw/ contiene AGENTS.md, SOUL.md, TOOLS.md y setup.ps1.
Los 12 skills son compatibles con OpenClaw via la especificación AgentSkills.

## Prerequisitos

- Claude Code instalado y autenticado
- ComfyUI instalado (local o remoto)
- FFmpeg en PATH
- PowerShell 7+
- Windows (adaptable a Linux/macOS)
