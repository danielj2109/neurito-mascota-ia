# Neurito: mascota virtual con cerebro

Neurito es una mascota virtual que toma decisiones con una red neuronal hecha a mano con NumPy y se muestra con Pygame.

## Partes del proyecto

- **Neurito 1.0 (`main.py`):** según su hambre, energía y aburrimiento, la red decide si Neurito debe comer, dormir o jugar.
- **Neurito 2.0 (`saltar.py`):** la red aprende cuándo saltar para esquivar obstáculos que llegan a distintas velocidades.

## Archivos

| Archivo | Descripción |
|---|---|
| `main.py` | Mascota que decide comer, dormir o jugar |
| `saltar.py` | Juego donde Neurito aprende a saltar |
| `salto_modelo.py` | Red neuronal del salto (3 → 12 → 1) |
| `salto_juego.py` | Física del salto y choques |
| `EJERCICIO.md` | Experimentos de Neurito 1.0 |
| `EJERCICIO_2.md` | Experimentos de Neurito 2.0 |
| `GUIA_SALTO.md` | Guía de Neurito 2.0 |
| `assets/` | Imágenes de Neurito y capturas de los experimentos |

## Cómo ejecutarlo

```bash
uv sync
uv run main.py
uv run saltar.py
```

## Controles de `saltar.py`

| Tecla | Función |
|---|---|
| `1` | Entrenar una época |
| `2` | Entrenar cien épocas |
| `3` | Entrenamiento continuo |
| `A` | Modo automático o manual |
| `Espacio` | Saltar manualmente |
| `C` | Reiniciar pista |
| `R` | Reiniciar cerebro |
| `Esc` | Salir |

## Tecnologías

Python 3.12, NumPy, Pygame y uv.
