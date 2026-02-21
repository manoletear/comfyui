# ¿Qué es ComfyUI?

ComfyUI es el motor de IA visual más potente y modular disponible. Permite diseñar y ejecutar pipelines avanzados de modelos de difusión usando una **interfaz de nodos/grafo/flowchart** sin necesidad de escribir código.

## Características Principales

- **Sistema de nodos**: conecta nodos visualmente para crear pipelines complejos
- - **Cola asíncrona**: gestiona múltiples generaciones en orden
  - - **Gestión inteligente de VRAM**: corre en GPUs desde 1GB con smart offloading
    - - **Soporte offline**: el core nunca descarga nada sin tu permiso
      - - **Multiplataforma**: Windows, Linux y macOS
       
        - ## Modelos Soportados
       
        - ### Imágenes
        - | Modelo | Descripción |
        - |--------|-------------|
        - | FLUX.1-dev | Fotorrealismo máximo, 16GB+ VRAM |
        - | FLUX Kontext | Edición iterativa de personajes |
        - | SDXL / RealVisXL | SDXL rápido, 8GB+ |
        - | SD1.5 | Clásico, ligero, compatible |
        - | HiDream, Lumina 2.0 | Modelos 2025 de alta calidad |
       
        - ### Video
        - | Modelo | Mejor Para | VRAM |
        - |--------|-----------|------|
        - | Wan 2.2 MoE 14B | Calidad cinematográfica | 24GB+ |
        - | FramePack | Videos largos, bajo VRAM | 6GB+ |
        - | AnimateDiff V3 | Iteración rápida | 8GB+ |
        - | Hunyuan Video | Videos largos de alta calidad | 24GB+ |
       
        - ### Audio / Voz
        - - Stable Audio, ACE Step
         
          - ### 3D
          - - Hunyuan3D 2.0
           
            - ## ¿Por qué usar ComfyUI?
           
            - A diferencia de otras UIs, ComfyUI te da **control total** sobre el pipeline de generación. Cada paso es un nodo: cargas el modelo, aplicas condicionamiento, decodificas el latente y guardas la imagen. Puedes ver exactamente qué ocurre en cada etapa y optimizar según tus necesidades.
