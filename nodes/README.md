# Nodos Personalizados para ComfyUI

Los nodos personalizados (custom nodes) extienden ComfyUI con funcionalidades adicionales.
Se instalan en la carpeta ComfyUI/custom_nodes/ y se activan al reiniciar.

## Nodos Esenciales

| Nodo | Función | Instalación |
|------|---------|-------------|
| ComfyUI-Manager | Gestión de nodos y modelos | git clone ltdrdata/ComfyUI-Manager |
| VideoHelperSuite | Workflows de video | git clone Kosinkadink/ComfyUI-VideoHelperSuite |
| IPAdapter Plus | Condicionamiento por imagen | git clone cubiq/ComfyUI_IPAdapter_plus |
| ControlNet | Control de composición | git clone Mikubill/sd-webui-controlnet |
| AnimateDiff | Animación de imágenes | git clone Kosinkadink/ComfyUI-AnimateDiff-Evolved |
| Impact Pack | Detección y máscaras | git clone ltdrdata/ComfyUI-Impact-Pack |

## Ver Documentación Detallada

- [ComfyUI-Manager](manager.md)
- [VideoHelperSuite](video-helper-suite.md)
- [IPAdapter Plus](ipadapter-plus.md)
- [comfyui-mcp](comfyui-mcp.md) - Control via Claude Code MCP
- [comfyui-openclaw-skill](comfyui-openclaw-skill.md) - Skill para OpenClaw

## Instalación Rápida via Manager

1. Abre ComfyUI con --enable-manager
2. Haz clic en "Manager" en el menú principal
3. Selecciona "Install Custom Nodes"
4. Busca el nodo y haz clic en Install
5. Reinicia ComfyUI
