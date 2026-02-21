# Workflows de ComfyUI

Los workflows son los pipelines de generación de ComfyUI guardados como JSON.
Se pueden cargar arrastrando el archivo al canvas o usando Ctrl+O.

## Formatos

### Formato UI
El formato que exporta la interfaz web de ComfyUI. Contiene arrays de nodos y links.
Archivo típico: my-workflow.json exportado desde el canvas.

### Formato API
El formato requerido para llamadas directas a /prompt. Node IDs como claves del objeto.
Usado por comfyui-mcp, comfyui-expert, comfyui-skill.

Para convertir entre formatos: /comfy:convert workflow.json (con comfyui-mcp)

## Organización de Este Repositorio

### text-to-image/
Workflows básicos de generación texto a imagen.
- flux-basic.json: Workflow FLUX.1-dev text-to-image
- sdxl-basic.json: Workflow SDXL estándar

### image-to-video/
Workflows para convertir imágenes a video.
- wan-2.2-i2v.json: Wan 2.2 image-to-video
- animatediff-motion.json: AnimateDiff con motion LoRA

### face-identity/
Workflows de preservación de identidad.
- ipadapter-face.json: IPAdapter portrait
- instantid-portrait.json: InstantID con FLUX

### upscaling/
Workflows para mejorar resolución.
- esrgan-upscale.json: Upscaling con ESRGAN

### voice-lipsync/
Workflows de síntesis de voz y lip-sync.
- wav2lip-pipeline.json: Lip-sync con Wav2Lip

### mcp-recipes/
Recetas multi-paso accesibles desde Claude Code.
Ver mcp-recipes/README.md para detalles.

## Cargar Workflows desde Imágenes

Las imágenes generadas con ComfyUI contienen el workflow embebido en metadata PNG.
Arrástralas al canvas para recuperar el workflow completo, incluyendo seeds.
Con comfyui-mcp: workflow_from_image para extraer vía API.

## Tips

- Usa validate_workflow (comfyui-mcp) antes de ejecutar para detectar errores
- Guarda seeds exitosos para poder reproducir resultados
- Los workflows pueden compartirse en comfyworkflows.com y openart.ai
