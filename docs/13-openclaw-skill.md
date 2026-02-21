# ComfyUI Skill para OpenClaw

## ¿Qué es OpenClaw?

Plataforma de agentes de IA alternativa a Claude Code. Los skills son módulos
de conocimiento en Markdown que el agente carga bajo demanda. Se instalan desde
ClawHub (clawhub.ai).

Repositorio: https://github.com/kelvincai522/comfyui-skill

## Instalación

npm i -g clawhub
clawhub install comfyui

O manualmente: git clone y coloca en skills/comfyui/ del workspace.

## Prerequisitos

- ComfyUI en ~/ComfyUI con venv
- Python 3 en ~/ComfyUI/venv/bin/python (NO usar python del sistema)
- ComfyUI corriendo en 127.0.0.1:8188

## Cómo Funciona

1. Agente lee el workflow JSON
2. Identifica nodos de prompt/sampler (sin asumir IDs fijos)
3. Edita prompt, estilo, seed en el JSON
4. Escribe a assets/tmp-workflow.json
5. Ejecuta comfyui_run.py -> entrega imagen al usuario

El script solo ejecuta. Toda la edición es responsabilidad del agente.

## Script: comfyui_run.py

Encola workflow y hace polling hasta completar.

~/ComfyUI/venv/bin/python skills/comfyui/scripts/comfyui_run.py --workflow path/to/workflow.json

Argumentos:
--workflow (requerido): Ruta al JSON en formato API
--host (default: 127.0.0.1): Host del servidor
--port (default: 8188): Puerto del servidor
--timeout (default: 300): Segundos máximos
--poll (default: 1.5): Segundos entre polls

Salida JSON:
{ "prompt_id": "abc123", "images": [{ "filename": "out.png", "subfolder": "", "type": "output" }] }

Ruta completa: ComfyUI/output/<subfolder>/<filename>

## Script: download_weights.py

Descarga modelos desde URLs a ~/ComfyUI/models/<subfolder>/.

Uso básico:
~/ComfyUI/venv/bin/python skills/comfyui/scripts/download_weights.py --base ~/ComfyUI https://example.com/model.safetensors

Desde stdin:
echo "https://example.com/model.safetensors" | ~/ComfyUI/venv/bin/python scripts/download_weights.py --base ~/ComfyUI

Subfolder manual:
--subfolder loras

Opciones:
--overwrite: Sobreescribir existentes
--no-pget: Usar descarga built-in

Subfolders soportados: checkpoints, clip, clip_vision, controlnet, diffusion_models,
embeddings, loras, text_encoders, unet, vae, vae_approx, upscale_models

Usa pget para descargas paralelas. Lo instala en ~/.local/bin si no está en PATH.

## Si el Servidor No Es Alcanzable

Si ComfyUI no está instalado:
git clone https://github.com/comfyanonymous/ComfyUI.git ~/ComfyUI
cd ~/ComfyUI
python3 -m venv venv
~/ComfyUI/venv/bin/pip install -r requirements.txt

Para iniciar:
~/ComfyUI/venv/bin/python ~/ComfyUI/main.py --listen 127.0.0.1

## Publicar en ClawHub

clawhub publish ./skills/comfyui --slug comfyui --name "ComfyUI" --version 1.0.1 --changelog "cambios"

Requiere cuenta GitHub con al menos 1 semana de antigüedad.

## Ver más

Referencia del nodo: nodes/comfyui-openclaw-skill.md
Script Python: scripts/comfyui_run.py
Comparativa: references/ai-agents-comparison.md
