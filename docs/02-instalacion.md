# Instalación de ComfyUI

## Método 1: Windows Portable (Recomendado para principiantes)

1. Descarga el paquete portable desde la [página de releases](https://github.com/comfyanonymous/ComfyUI/releases)
2. Extrae con 7-Zip o el explorador de Windows
3. Coloca tus modelos en ComfyUI/models/checkpoints
4. Ejecuta run_nvidia_gpu.bat (o run_cpu.bat si no tienes GPU)

## Método 2: comfy-cli (Recomendado)

pip install comfy-cli && comfy install

## Método 3: Instalación Manual

Requisitos: Python 3.13, PyTorch 2.4+, Git

git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130
pip install -r requirements.txt
python main.py

## Flags de Lanzamiento

--highvram: GPUs 24GB+
--lowvram: GPUs con poca VRAM
--cpu: Sin GPU
--fp8_e4m3fn-unet: Cuantización RTX 5090
--preview-method taesd: Previews HD
--enable-manager: ComfyUI Manager
--listen: Acceso remoto

## Por GPU

NVIDIA: pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130
AMD Linux: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm7.1
Intel Arc: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/xpu
Apple M1/M2: instalar PyTorch nightly con MPS y ejecutar python main.py

## Estructura de Carpetas de Modelos

ComfyUI/models/ - checkpoints, vae, loras, controlnet, ipadapter, clip_vision, upscale_models, vae_approx

## Instalación de ComfyUI-Manager

cd ComfyUI/custom_nodes
git clone https://github.com/ltdrdata/ComfyUI-Manager comfyui-manager
python main.py --enable-manager
