# Integración ComfyUI + MCP + Claude Code

## ¿Qué es comfyui-mcp?

Servidor MCP (Model Context Protocol) y plugin para Claude Code que convierte a Claude
en un asistente capaz de controlar ComfyUI directamente desde el chat.

Repositorio: https://github.com/artokun/comfyui-mcp

## Instalación

Añade a ~/.claude/settings.json:

{
  "mcpServers": {
    "comfyui": {
      "command": "npx",
      "args": ["-y", "comfyui-mcp"],
      "env": {
        "CIVITAI_API_TOKEN": ""
      }
    }
  }
}

Como plugin: claude plugin install comfyui-mcp

## Requisitos

- Node.js >= 22.0.0
- ComfyUI corriendo localmente (puerto 8188 o 8000)
- Claude Code instalado y autenticado

## Variables de Entorno

| Variable | Default | Descripción |
|----------|---------|-------------|
| COMFYUI_HOST | 127.0.0.1 | Dirección del servidor |
| COMFYUI_PORT | auto | Puerto (prueba 8188, luego 8000) |
| COMFYUI_PATH | auto | Ruta al directorio de datos |
| CIVITAI_API_TOKEN | — | Token para CivitAI |
| HUGGINGFACE_TOKEN | — | Token para HuggingFace |
| GITHUB_TOKEN | — | Token para generación de skills |
| LOG_LEVEL | info | debug, info, warn, error |

## Cómo Funciona

Claude Code (chat)
  -> MCP Protocol (stdio)
  -> comfyui-mcp server
     -> REST API: /object_info, /history, /queue, /free
     -> WebSocket: progreso en tiempo real
     -> File System: models/, output/, input/
     -> APIs externas: HuggingFace, Registry, CivitAI

## Capacidades

| Categoría | Cantidad |
|-----------|----------|
| MCP Tools | 31 |
| Slash Commands | 10 |
| Skills de conocimiento | 4 |
| Agentes autónomos | 3 |
| Hooks | 3 |

## Los 3 Agentes Autónomos

comfy-explorer: Investiga packs de nodos, genera skill files
comfy-debugger: Diagnostica fallas automáticamente
comfy-optimizer: Analiza y optimiza workflows

## Los 3 Hooks

VRAM Watchdog: Avisa si VRAM < 1GB antes de ejecutar
Save Warning: Pregunta sobre cambios sin guardar antes de stop
Job Notify: Inyecta resumen de jobs completados

## Las 4 Skills de Conocimiento

comfyui-core: Formato workflow, tipos de nodos, arquitectura
prompt-engineering: Sintaxis CLIP, embeddings, prompting por modelo
troubleshooting: Catálogo de errores OOM, dtype, nodos faltantes
model-compatibility: Compatibilidad loaders/samplers/CFG por familia

## Seguimiento SQLite (generations.db)

Cada enqueue_workflow se registra automáticamente.
Modelos identificados por hash SHA256, no por nombre.
suggest_settings recomienda config basado en historial local.
Ver stats: npm run generations:stats

## Troubleshooting

"ComfyUI not detected": Verifica que ComfyUI esté corriendo, define COMFYUI_PORT
"COMFYUI_PATH not configured": Define COMFYUI_PATH apuntando a carpeta con models/
Model downloads fail: Define HUGGINGFACE_TOKEN o CIVITAI_API_TOKEN
OOM: Usa clear_vram, el VRAM watchdog avisa automáticamente

## Ver más

Referencia 31 tools: references/mcp-tools.md
Slash commands: references/mcp-slash-commands.md
Comparativa agentes: references/ai-agents-comparison.md
