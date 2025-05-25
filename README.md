Proyecto de comparación de rendimiento # VM vs Docker

Este proyecto compara el uso de recursos y las métricas de rendimiento entre una máquina virtual completa (VirtualBox) y un contenedor Docker.

## Índice de Documentos

1. [Documento 1: Informe Técnico](https://docs.google.com/document/d/1ZKTfD3cAN7Y1vyLOoTKwYFgKzRSr_D_SWBL-7WP90Nw/edit?usp=sharing)
2. [Documento 2: Manual de Usuario](https://github.com/ElNavas-8/Proyecto_TIC/blob/main/scripts/README.md)

---

## 🔧 Estructura del proyecto
notebooks/: Jupyter Notebook para ejecutar y trazar benchmarks.

scripts/: Scripts de configuración para la máquina virtual, Docker y el propio Dockerfile

results/: Marcador de posición para los resultados del benchmark

## 📦 Requisitos
Python 3.8+

Docker (host o WSL2)

VirtualBox (con un invitado Linux)

sysbench, jupyter, matplotlib, psutil

## 🚀 Inicio rápido En VM o Docker

cd scripts

[Levantar el proyecto](https://github.com/ElNavas-8/Proyecto_TIC/blob/main/scripts/README.md)

bash stats.py # Para VM

bash stats.py # Para Docker o WSL2
