# Hardware y Requisitos de VRAM

## Guía por GPU

### RTX 5090 (32GB VRAM) — Perfil de referencia
| Tarea | Estado | Notas |
|-------|--------|-------|
| FLUX.1-dev FP16 | OK Nativo | Sin cuantización |
| Wan 2.2 14B | OK Nativo | Calidad completa |
| FramePack | OK Exceso | Diseñado para 6GB |
| PuLID Flux II | OK Nativo | Generación dual |
| InfiniteYou | OK Nativo | Ambas variantes |
| LoRA Training FLUX | OK Nativo | Sin cuantización |

Flags recomendados: python main.py --highvram --fp8_e4m3fn-unet

### RTX 4090 (24GB VRAM)
| Tarea | Estado |
|-------|--------|
| FLUX.1-dev FP16 | OK Nativo |
| Wan 2.2 14B | OK Nativo |
| LoRA Training FLUX | OK Con ajustes |

### RTX 4080 / 4070 Ti (16GB VRAM)
| Tarea | Estado |
|-------|--------|
| FLUX.1-dev FP8 | OK Cuantizado |
| SDXL / RealVisXL | OK Nativo |
| Wan 2.2 (versión pequeña) | Ajustado |

### RTX 3080 / 4070 (10-12GB VRAM)
| Tarea | Estado |
|-------|--------|
| SDXL | OK Nativo |
| FLUX cuantizado Q4 | Lento |
| AnimateDiff | OK Con --lowvram |

### RTX 3060 / 4060 (8GB VRAM)
- Usar --lowvram
- SDXL funciona bien
- AnimateDiff con batches pequeños
- FramePack funciona perfectamente

### GPUs de 6GB o menos
- Usar --lowvram o --novram
- SD1.5 funciona bien
- FramePack: diseñado para este rango
- SDXL: posible con offloading agresivo

## Configuración por Escenario

Alta VRAM (24GB+): python main.py --highvram
VRAM media (8-16GB): python main.py
VRAM baja (<8GB): python main.py --lowvram
Sin GPU: python main.py --cpu
