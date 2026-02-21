# comfyui-mcp — Servidor MCP para ComfyUI

Plugin y servidor MCP que permite controlar ComfyUI desde Claude Code con 31 herramientas, 10 slash commands, 3 agentes y 4 skills de conocimiento.

Repositorio: https://github.com/artokun/comfyui-mcp

## Instalación rápida

Añade a ~/.claude/settings.json:

{
  "mcpServers": {
    "comfyui": {
      "command": "npx",
      "args": ["-y", "comfyui-mcp"],
      "env": {
        "CIVITAI_API_TOKEN": "tu_token"
      }
    }
  }
}

Como plugin: claude plugin install comfyui-mcp

## Slash Commands

/comfy:gen "descripción de imagen" - Genera imagen automáticamente
/comfy:viz workflow.json - Visualiza como diagrama Mermaid
/comfy:debug - Diagnostica último fallo
/comfy:debug <prompt_id> - Diagnostica por ID
/comfy:batch "prompt, cfg:5-10:2, sampler:euler" - Barrido de parámetros
/comfy:convert workflow.json - Convierte entre formatos UI y API
/comfy:install <pack> - Instala nodo desde registro
/comfy:gallery last 10 - Navega imágenes generadas
/comfy:compare a.json vs b.json - Compara workflows
/comfy:recipe portrait "mi prompt" - Pipelines multi-paso
/comfy:node-skill <pack> - Genera skill para nodo

## Las 31 Herramientas MCP (resumen)

Ejecución: enqueue_workflow, get_job_status, get_queue, cancel_job, get_system_stats
Visualización: visualize_workflow, mermaid_to_workflow
Composición: create_workflow, modify_workflow, get_node_info
Validación: validate_workflow
Biblioteca: list_workflows, get_workflow, save_workflow
Imágenes: upload_image, workflow_from_image, list_output_images
Modelos: search_models, download_model, list_local_models
Memoria: clear_vram, get_embeddings
Registro: search_custom_nodes, get_node_pack_details, generate_node_skill
Diagnóstico: get_logs, get_history
Proceso: stop_comfyui, start_comfyui, restart_comfyui
Generaciones: suggest_settings, generation_stats

## Los 3 Agentes Autónomos

comfy-explorer: Investiga packs de nodos, genera skill files
comfy-debugger: Diagnostica fallas de workflow automáticamente
comfy-optimizer: Analiza y optimiza workflows para rendimiento y VRAM

## Los 3 Hooks

VRAM Watchdog: Avisa si VRAM libre < 1GB antes de ejecutar
Save Warning: Pregunta si hay cambios sin guardar antes de stop/restart
Job Notify: Inyecta resumen de trabajos completados

## Las 4 Skills de Conocimiento

comfyui-core: Formato workflow, tipos de nodos, flujo de datos
prompt-engineering: Sintaxis CLIP, tokens BREAK, prompting por modelo
troubleshooting: Catálogo de errores con soluciones
model-compatibility: Compatibilidad por familia de modelo

## Seguimiento SQLite

Cada generación se registra en generations.db con hash del modelo.
Usa suggest_settings para recomendaciones basadas en historial.
Ver stats: npm run generations:stats

## Ver más

Guía completa: docs/12-mcp-integration.md
Referencia 31 tools: references/mcp-tools.md
Slash commands: references/mcp-slash-commands.md
