import nbformat

from milestone1 import cells

nb = nbformat.v4.new_notebook()

nb.cells = cells()

with open("../notebook/k2pdfopt_colab.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("Notebook written.")