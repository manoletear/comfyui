# ComfyUI Knowledge Base

Base de conocimiento completa sobre ComfyUI — el motor de IA visual más poderoso y modular.

## ¿Qué es este repositorio?

Reúne documentación, workflows, referencias de modelos y scripts para trabajar con ComfyUI
de forma profesional. Cubre desde instalación básica hasta pipelines avanzados de video, voz
y entrenamiento de LoRAs. Incluye documentación de integraciones con agentes IA.

## Estructura

| Carpeta | Contenido |
|---------|-----------|
| docs/ | Documentación completa por tema (13 archivos) |
| nodes/ | Guías de nodos personalizados esenciales |
| workflows/ | Workflows JSON listos para usar |
| models/ | Catálogos y guías de modelos |
| scripts/ | Scripts de utilidad (incluyendo comfyui_run.py) |
| comfyui-expert/ | Documentación del orquestador VideoAgent (MCKRUZ) |
| references/ | Atajos, API, comparativa de integraciones |

## Inicio Rápido

1. Lee docs/02-instalacion.md para instalar ComfyUI
2. Instala el Manager: nodes/manager.md
3. Carga un workflow desde workflows/
4. Consulta docs/10-hardware-vram.md según tu GPU

## Documentación (docs/)

- 01-introduccion.md: ¿Qué es ComfyUI? Modelos soportados
- 02-instalacion.md: Instalación Windows, Linux, macOS
- 04-modelos.md: Catálogo de modelos imagen, video, voz
- 10-hardware-vram.md: Requisitos por GPU
- 11-troubleshooting.md: Solución de problemas comunes
- 12-mcp-integration.md: ComfyUI + MCP + Claude Code
- 13-openclaw-skill.md: Skill para OpenClaw

## Integraciones con Agentes IA

Este repositorio documenta tres integraciones para controlar ComfyUI desde agentes IA:

### ComfyUI-Expert (MCKRUZ) - comfyui-expert/
Orquestador de sesión para Claude Code con 12 skills especializados en producción de video.
Repositorio: https://github.com/MCKRUZ/ComfyUI-Expert

### comfyui-mcp (artokun) - docs/12-mcp-integration.md
Servidor MCP con 31 herramientas, 10 slash commands, 3 agentes y 4 skills de conocimiento.
Instalación: npx comfyui-mcp o claude plugin install comfyui-mcp
Repositorio: https://github.com/artokun/comfyui-mcp

### comfyui-skill (kelvincai522) - docs/13-openclaw-skill.md
Skill para OpenClaw: ejecuta workflows via HTTP API con Python puro (sin dependencias).
Instalación: clawhub install comfyui
Repositorio: https://github.com/kelvincai522/comfyui-skill

Comparativa completa: references/ai-agents-comparison.md

## Modelos Cubiertos

Imágenes: FLUX.1-dev, FLUX Kontext, SDXL, RealVisXL, SD1.5, HiDream
Video: Wan 2.2, FramePack, AnimateDiff V3, Hunyuan Video
Voz/TTS: Chatterbox, F5-TTS, TTS Audio Suite, ElevenLabs, RVC
Lip-Sync: LatentSync 1.6, Wav2Lip, SadTalker, LivePortrait
Identidad: InstantID, IPAdapter Plus, PuLID, InfiniteYou

## Nodos Documentados

- ComfyUI-Manager: Gestión de nodos y modelos
- VideoHelperSuite: Load/Combine video
- IPAdapter Plus: Condicionamiento por imagen de referencia
- comfyui-mcp: Control completo vía Claude Code MCP
- comfyui-openclaw-skill: Skill para plataforma OpenClaw

## Créditos

- Comfy-Org/ComfyUI: https://github.com/comfyanonymous/ComfyUI
- ComfyUI-Manager: https://github.com/ltdrdata/ComfyUI-Manager
- MCKRUZ/ComfyUI-Expert: https://github.com/MCKRUZ/ComfyUI-Expert
- artokun/comfyui-mcp: https://github.com/artokun/comfyui-mcp
- kelvincai522/comfyui-skill: https://github.com/kelvincai522/comfyui-skill
- VideoHelperSuite: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite
- IPAdapter Plus: https://github.com/cubiq/ComfyUI_IPAdapter_plus# comfyui
