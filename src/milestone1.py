from nbformat.v4 import new_markdown_cell, new_code_cell


def cells():
    return [

        new_markdown_cell(r"""
# k2pdfopt Google Colab

## Milestone 1

This notebook downloads the official **k2pdfopt** Linux executable,
verifies that it works, and prepares the environment for PDF conversion.
"""),

        new_code_cell(r"""
print("=" * 60)
print("Environment")
print("=" * 60)

import platform

print("Python :", platform.python_version())
print("Platform :", platform.platform())
"""),

        new_markdown_cell("## Install download utility"),

        new_code_cell(r"""
!pip -q install gdown
"""),

        new_markdown_cell("## Download k2pdfopt"),

        new_code_cell(r"""
import os
import gdown

FILE_ID = "1WhfSKt52raKtg1y1Y-55pvly-XOmLYLc"

url = f"https://drive.google.com/uc?id={FILE_ID}"

gdown.download(url, "k2pdfopt", quiet=False)

assert os.path.exists("k2pdfopt"), "Download failed."

print("Download completed.")
"""),

        new_markdown_cell("## Make executable"),

        new_code_cell(r"""
!chmod +x k2pdfopt

import os

assert os.access("k2pdfopt", os.X_OK), "Executable permission not set."

print("Executable permission granted.")
"""),

        new_markdown_cell("## Verify"),

        new_code_cell(r"""
!./k2pdfopt -?
"""),

        new_markdown_cell(r"""
# ✅ Milestone 1 Complete

The k2pdfopt executable has been downloaded and verified.

The next milestone will:

1. Upload a PDF.
2. Convert it with k2pdfopt.
3. Download the converted PDF.
""")
    ]