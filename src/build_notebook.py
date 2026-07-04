from pathlib import Path
import nbformat

from milestone1 import cells

ROOT = Path(__file__).resolve().parent.parent

NOTEBOOK = ROOT / "notebook" / "k2pdfopt_colab.ipynb"

nb = nbformat.v4.new_notebook()
nb.cells = cells()

with NOTEBOOK.open("w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"Notebook written to {NOTEBOOK}")