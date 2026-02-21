# API REST de ComfyUI

ComfyUI expone una API REST en http://127.0.0.1:8188 por defecto.
Esta API es usada por todas las integraciones (comfyui-mcp, comfyui-expert, comfyui-skill).

## Endpoints Principales

### POST /prompt
Encola un workflow para ejecución.

Request body:
{
  "client_id": "uuid-único",
  "prompt": { ...workflow_json_en_formato_API... }
}

Response:
{
  "prompt_id": "abc123",
  "number": 5,
  "node_errors": {}
}

### GET /history/{prompt_id}
Verifica el estado de ejecución de un job.

Response cuando completo:
{
  "abc123": {
    "status": { "completed": true },
    "outputs": {
      "9": {
        "images": [
          { "filename": "ComfyUI_00001_.png", "subfolder": "", "type": "output" }
        ]
      }
    }
  }
}

### GET /queue
Ver la cola de ejecución actual (running + pending).

### POST /interrupt
Cancela el job en ejecución actual.

### GET /system_stats
Información del sistema: GPU, VRAM, Python, OS.

### GET /object_info
Lista todos los tipos de nodos disponibles con sus inputs/outputs.
Usado por comfyui-mcp para validación y composición de workflows.

### POST /free
Libera la VRAM descargando modelos en caché.

Body: { "unload_models": true, "free_memory": true }

### GET /history
Lista el historial completo de ejecuciones.

### POST /upload/image
Sube una imagen al directorio input/ de ComfyUI.
Tipo: multipart/form-data con el campo "image".

## Formato de Workflow (API)

El formato API difiere del formato UI de ComfyUI.
En formato API, cada nodo tiene un ID numérico y esta estructura:

{
  "1": {
    "class_type": "CheckpointLoaderSimple",
    "inputs": {
      "ckpt_name": "v1-5-pruned-emaonly.ckpt"
    }
  },
  "2": {
    "class_type": "CLIPTextEncode",
    "inputs": {
      "clip": ["1", 1],
      "text": "a beautiful landscape"
    }
  }
}

Las referencias a salidas de otros nodos usan el formato ["node_id", output_index].

## Conversión UI <-> API

Usa /comfy:convert desde comfyui-mcp para convertir entre formatos.
O usa la herramienta convert del servidor MCP directamente.

## Polling recomendado

Encola con POST /prompt -> obtén prompt_id
Haz polling a GET /history/{prompt_id} cada 1-2 segundos
Cuando status.completed == true, lee outputs.{node_id}.images
