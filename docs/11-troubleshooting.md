# Solución de Problemas Comunes

## Errores de VRAM (OOM - Out of Memory)

Síntomas: CUDA out of memory, RuntimeError: CUDA error
Soluciones:
- Cambiar a --lowvram o --novram
- Usar modelos cuantizados (FP8 en vez de FP16)
- Cerrar otras aplicaciones que usen GPU
- Para ComfyUI-MCP: usar clear_vram antes de ejecutar

## Nodos Faltantes (Missing Nodes)

Síntomas: ERROR: Node type not found
Soluciones:
- Instalar ComfyUI-Manager y buscar el nodo faltante
- Usar /comfy:install <pack> desde Claude Code con MCP
- Buscar el nodo en https://registry.comfy.org

## Error: Torch not compiled with CUDA

pip uninstall torch
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130

## Imágenes Negras o Completamente Grises

Causas:
- VAE incorrecto para el modelo
- CFG demasiado alto (probar 1-7 para FLUX)
- CLIP skip incorrecto

## Error: No module named 'xxx'

pip install -r requirements.txt
(En el entorno correcto de Python/venv)

## ComfyUI No Inicia

- Verificar que Python 3.12-3.13 esté instalado
- Verificar que PyTorch 2.4+ esté instalado
- Revisar logs en terminal para error específico

## Cara Quemada (Burned Face)

En workflows de preservación de identidad:
- Bajar el peso de IPAdapter a 0.6-0.8
- Usar face_only en vez del modelo completo
- Probar con diferentes seeds

## Precisión Incorrecta (dtype mismatch)

- Asegurarse de que VAE y modelo usen la misma precisión
- Usar --fp16-vae o desactivar según el modelo
- Para FLUX: usar el VAE específico de FLUX

## Workflow Válido Pero No Ejecuta

1. Verificar con validate_workflow (comfyui-mcp)
2. Revisar que todos los modelos existan en los paths correctos
3. Verificar conexiones entre nodos
4. Ejecutar /comfy:debug desde Claude Code

## Rendimiento Lento

- Activar previews TAESD: --preview-method taesd
- Verificar que GPU está siendo usada (no CPU)
- Para AMD: HSA_OVERRIDE_GFX_VERSION=10.3.0 python main.py
- Reducir resolución de generación
- Usar modelos cuantizados

## ComfyUI-Manager No Aparece

- Verificar que está en ComfyUI/custom_nodes/comfyui-manager
- Reiniciar con: python main.py --enable-manager
- Si falla: cd custom_nodes/comfyui-manager && git pull
