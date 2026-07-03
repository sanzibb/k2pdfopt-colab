from nbformat.v4 import new_markdown_cell
from nbformat.v4 import new_code_cell


def cells():
    return [

        new_markdown_cell(r"""
# Milestone 1

## Goal

Compile **k2pdfopt** from official source in a fresh Google Colab runtime.

If this notebook finishes successfully, we know the build
environment is reproducible.
"""),

        new_code_cell(r"""
import os
import platform
import subprocess

print("="*60)
print("System Information")
print("="*60)

print("Platform :", platform.platform())
print("Python   :", platform.python_version())

print("\nCPU")
subprocess.run(["lscpu"])

print("\nMemory")
subprocess.run(["free","-h"])
"""),

        new_markdown_cell("## Install build dependencies"),

        new_code_cell(r"""
!apt-get update

!apt-get install -y \
    build-essential \
    cmake \
    git \
    pkg-config \
    wget \
    curl \
    ca-certificates \
    zlib1g-dev \
    libpng-dev \
    libjpeg-dev \
    libopenjp2-7-dev \
    libdjvulibre-dev \
    libfreetype6-dev \
    libgsl-dev \
    libleptonica-dev \
    libtesseract-dev \
    ghostscript
"""),

        new_markdown_cell("## Download Debian source package"),

        new_code_cell(r"""
!apt-get install -y dpkg-dev

!apt-get source k2pdfopt
"""),

        new_markdown_cell("## Locate extracted source"),

        new_code_cell(r"""
from pathlib import Path

dirs = sorted(Path(".").glob("k2pdfopt-*"))

assert len(dirs) > 0

SOURCE_DIR = str(dirs[0])

print(SOURCE_DIR)
"""),

        new_markdown_cell("## Configure"),

        new_code_cell(r"""
%cd $SOURCE_DIR

!mkdir -p build

%cd build

!cmake ..
"""),

        new_markdown_cell("## Build"),

        new_code_cell(r"""
import multiprocessing

cores = multiprocessing.cpu_count()

print("CPU cores:", cores)

!make -j{cores}
"""),

        new_markdown_cell("## Verify executable"),

        new_code_cell(r"""
import os

exe="./k2pdfopt"

assert os.path.exists(exe)

print("Executable created.")
"""),

        new_markdown_cell("## Display version"),

        new_code_cell(r"""
!./k2pdfopt -h | head -40
""")
    ]