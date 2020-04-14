if [ ! -d "./.venv/notebooks "]
then
    mkdir -p ./.venv
    python3 -m venv ./.venv/notebooks
fi

source ./.venv/notebooks/bin/activate

pip install -r requirements.txt

pip install --editable .

# Jupyter widgets extension
jupyter labextension install @jupyter-widgets/jupyterlab-manager@1.1 --no-build

# FigureWidget support
jupyter labextension install plotlywidget@4.6.0 --no-build

# and jupyterlab renderer support
jupyter labextension install jupyterlab-plotly@4.6.0 --no-build

jupyter labextension install @jupyterlab/toc --no-build

# Build extensions (must be done to activate extensions since --no-build is used above)
jupyter lab build

jupyter lab