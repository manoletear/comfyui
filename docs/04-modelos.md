# Catálogo de Modelos para ComfyUI

## Generación de Imágenes

### FLUX.1-dev
- Uso: Fotorrealismo, máxima calidad
- VRAM: 16GB+ (FP16), 8GB (FP8 cuantizado)
- Descarga: https://huggingface.co/black-forest-labs/FLUX.1-dev

### FLUX Kontext
- Uso: Edición iterativa de personajes, consistencia de identidad
- VRAM: 12-32GB
- Mejor para: Modificar imágenes existentes sin reentrenar

### RealVisXL V5.0
- Uso: Fotorrealismo rápido con SDXL
- VRAM: 8GB+

## Preservación de Identidad

| Método | Mejor Para | VRAM |
|--------|-----------|------|
| InfiniteYou | Mayor fidelidad de identidad | 24GB |
| FLUX Kontext | Edición sin reentrenar | 12-32GB |
| PuLID Flux II | Personajes duales | 24-40GB |
| IPAdapter Face | Portraits | 8GB+ |
| InstantID | Preservación rápida | 16GB+ |

## Generación de Video

### Wan 2.2 MoE 14B
- Calidad: Cinematográfica
- VRAM: 24GB+
- Clips: 5-10 segundos

### FramePack
- VRAM: desde 6GB
- Videos: 60+ segundos

### AnimateDiff V3
- Velocidad: La más rápida (4-8 steps Lightning)
- VRAM: 8GB+

## Síntesis de Voz y Lip-Sync

### TTS / Clonación de Voz
| Herramienta | Idiomas | Licencia |
|-------------|---------|---------|
| Chatterbox | Emotion tags | MIT |
| F5-TTS | Zero-shot, más rápido | MIT |
| TTS Audio Suite | 23 idiomas | Multi |
| IndexTTS-2 | Alta calidad | - |
| ElevenLabs | Comercial | Propietario |
| RVC | Voice conversion | MIT |

### Lip-Sync
| Herramienta | Características |
|-------------|----------------|
| LatentSync 1.6 | Mayor precisión (ByteDance) |
| Wav2Lip | Probado, cualquier cara |
| SadTalker | Movimiento cabeza + expresiones |
| LivePortrait | Transferencia de expresión |

## Modelos 3D
- Hunyuan3D 2.0

## Modelos de Audio
- Stable Audio
- ACE Step
