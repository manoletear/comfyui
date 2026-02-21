# ComfyUI-Manager

Extensión esencial para gestionar nodos personalizados en ComfyUI.

Repositorio: https://github.com/ltdrdata/ComfyUI-Manager

## Instalación

cd ComfyUI/custom_nodes
git clone https://github.com/ltdrdata/ComfyUI-Manager comfyui-manager

Luego reinicia con: python main.py --enable-manager

## Funcionalidades

- Install Custom Nodes: Busca e instala nodos desde el registro oficial
- Install Models: Descarga modelos directamente
- Snapshot Manager: Guarda y restaura estados de instalación
- Update All: Actualiza todos los nodos instalados
- Fix Node (Recreate): Repara nodos de workflows antiguos

## Modos de Base de Datos

| Modo | Descripción |
|------|-------------|
| DB: Channel (1day cache) | Default. Cache de 1 día |
| DB: Local | Solo información local |
| DB: Channel (remote) | Lista más reciente siempre |

## Niveles de Seguridad (config.ini)

- strong: Solo operaciones de bajo riesgo
- normal: Bloquea instalaciones de alto riesgo (default)
- normal-: Más permisivo en red local
- weak: Todo permitido

## Variables de Entorno

- COMFYUI_PATH: Ruta de instalación de ComfyUI
- GITHUB_ENDPOINT: Proxy para GitHub
- HF_ENDPOINT: Proxy para Hugging Face

## Snapshot Manager

Guarda snapshots con Save snapshot o Update All.
Restaura con el botón Restore en la lista de snapshots.
Los snapshots se guardan en <USER_DIR>/default/ComfyUI-Manager/snapshots/
