# Scripts de Utilidad

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
