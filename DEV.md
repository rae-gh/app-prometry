# Locally install and run for DEV

1. Create a conda environment:

```bash
conda create -n prom-env python=3.12 -y
conda activate prom-env
```

2. Install the required packages:

```bash
# IMPORTANT: Make sure conda environment is activated first!
conda activate prom-env
pip install -r requirements.txt
```

> **Note**: If you get `ModuleNotFoundError: No module named 'maptial'`, ensure all packages are installed in the conda environment, not in user site-packages. You can reinstall streamlit in the conda environment with:
> ```bash
> conda run -n prom-env pip install --force-reinstall streamlit
> ```

3. Run the Streamlit application:

```bash
# Option 1: Activate environment first (recommended)
conda activate prom-env
python -m streamlit run app/Home.py

# Option 2: Run without activating
conda run -n prom-env streamlit run app/Home.py
```


# Manually build mkdocs
1. Install MkDocs and dependencies
pip install mkdocs mkdocs-material mkdocstrings[python] pymdown-extensions

2. Serve locally (with live reload)
mkdocs serve

3. Build static site
mkdocs build

4. Deploy to GitHub Pages
mkdocs gh-deploy