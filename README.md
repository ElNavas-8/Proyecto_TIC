# Documentación del Proyecto

Bienvenido a la documentación del proyecto. A continuación, encontrarás enlaces a documentos clave que forman parte de este repositorio.

## Índice de Documentos

1. [Documento 1: Informe Técnico](https://docs.google.com/document/d/1ZKTfD3cAN7Y1vyLOoTKwYFgKzRSr_D_SWBL-7WP90Nw/edit?usp=sharing)
2. [Documento 2: Manual de Usuario](https://github.com/ElNavas-8/Proyecto_TIC/blob/main/scripts/README.md)

---

### Cómo usar esta documentación

- Haz clic en cualquiera de los enlaces anteriores para acceder al documento correspondiente.
- Asegúrate de tener acceso a los enlaces si están alojados en una plataforma privada (como Google Drive, Dropbox, etc.).

---

### Contacto

Para cualquier duda o sugerencia, por favor contacta al autor del proyecto o abre un *issue* en este repositorio.

# VM vs Docker Performance Benchmark Project

This project compares resource usage and performance metrics between a full virtual machine (VirtualBox) and a Docker container.

## 🔧 Project Structure
notebooks/: Jupyter Notebook for running and plotting benchmarks
scripts/: Setup scripts for VM, Docker, and Dockerfile itself
results/: Placeholder for benchmark results

## 📦 Requirements
Python 3.8+
Docker (host or WSL2)
VirtualBox (with a Linux guest)
sysbench, jupyter, matplotlib, psutil

## 🚀 Quick Start
bash
# On VM or Docker:
cd scripts
bash vm_setup.sh      # For VirtualBox
bash docker_setup.sh  # For Docker or WSL2
