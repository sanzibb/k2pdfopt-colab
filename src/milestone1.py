from nbformat.v4 import new_markdown_cell, new_code_cell


def cells():
    return [

        new_markdown_cell(
r"""
# k2pdfopt Google Colab

## Milestone 1

This notebook compiles **k2pdfopt** from source and verifies that the executable works.

If this notebook completes successfully, the build environment is ready for PDF conversion.
"""
        ),

        new_code_cell(
r"""
print("=" * 60)
print("Checking Environment")
print("=" * 60)

import platform
import subprocess

print("Python :", platform.python_version())
print("Platform :", platform.platform())

print("\nCPU")
subprocess.run(["lscpu"])

print("\nMemory")
subprocess.run(["free", "-h"])
"""
        ),

        new_markdown_cell(
"""
## Install build tools
"""
        ),

        new_code_cell(
r"""
!apt-get update
!apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    curl
"""
        ),

        new_markdown_cell(
"""
## Next step

The remaining notebook cells (download source, compile, verify) will be added in the next update.
"""
        )
    ]