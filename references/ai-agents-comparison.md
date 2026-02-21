# Comparativa: Integraciones de IA con ComfyUI

Este repositorio documenta cuatro aproximaciones para controlar ComfyUI desde agentes de IA.

## Tabla Comparativa

| Aspecto | ComfyUI-Expert (MCKRUZ) | comfyui-mcp (artokun) | comfyui-skill (kelvincai522) |
|---------|------------------------|----------------------|------------------------------|
| Plataforma | Claude Code | Claude Code + MCP | OpenClaw |
| Protocolo | CLAUDE.md routing | stdio MCP protocol | HTTP directo + stdin |
| Lenguaje | PowerShell + Markdown | TypeScript / Node.js | Python puro (stdlib) |
| Distribución | Git clone | npx / claude plugin install | clawhub install |
| Skills/Tools | 12 skills especializados | 31 MCP tools + 10 slash cmds | 1 skill + 2 scripts |
| Agentes | 1 orquestador | 3 autónomos | No |
| Hooks | 1 (staleness check) | 3 (VRAM, save, notify) | No |
| Base de datos | JSON (inventory, session) | SQLite (generations.db) | Ninguna |
| Descarga modelos | Referencia HuggingFace | download_model HF API | download_weights.py + pget |
| Seguimiento | No | Sí (hash modelo, reuse_count) | No |
| Dependencias | PowerShell 7+, FFmpeg | Node.js >= 22 | Python 3 stdlib |
| OS | Windows (bat), adaptable | macOS, Linux, Windows | macOS, Linux, Windows |
| Visualización | No | Mermaid diagrams | No |
| Caso ideal | Producción de video | Dev workflow / exploración | Uso simple con OpenClaw |
| Cruzado | También OpenClaw | Solo Claude Code/MCP | Solo OpenClaw |

## ¿Cuál usar?

### ComfyUI-Expert (MCKRUZ) si...
- Trabajas con producción de video con IA (Wan, FramePack, AnimateDiff)
- Necesitas pipeline completo: imagen, video, voz, lip-sync, publicación
- Usas Claude Code con flujos repetitivos de video

### comfyui-mcp (artokun) si...
- Quieres control universal de ComfyUI desde Claude Code
- Necesitas descubrir modelos, nodos y workflows interactivamente
- Te interesa el seguimiento histórico de generaciones con estadísticas

### comfyui-skill (kelvincai522) si...
- Usas la plataforma OpenClaw en vez de Claude Code
- Quieres solución minimalista sin dependencias (Python stdlib)
- Solo necesitas: ejecutar workflows + descargar modelos

## API REST Compartida

Todos los sistemas usan los mismos endpoints de ComfyUI:

| Endpoint | Método | Uso |
|----------|--------|-----|
| /prompt | POST | Encolar workflow |
| /history/{id} | GET | Estado de ejecución |
| /queue | GET | Ver cola |
| /system_stats | GET | Info GPU/VRAM |
| /object_info | GET | Nodos disponibles |
| /free | POST | Liberar VRAM |
| /interrupt | POST | Cancelar ejecución |

Ver referencia completa en references/api-reference.md
