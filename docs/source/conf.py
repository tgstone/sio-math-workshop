# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath('../..'))


project = 'sio_math_workshop'
copyright = '2025, Tommy Stone'
author = 'Tommy Stone'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser", # Markdwon
    "nbsphinx",    # Jupyter Notebooks
    'sphinx.ext.mathjax',
    "sphinx_rtd_theme", 
]

myst_enable_extensions = [
    "amsmath"
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
#html_static_path = ['_static']
## Use Read the Docs theme
## html_theme = "piccolo_theme"
html_theme = "furo"
html_static_path = ["_static"]
html_favicon = '_static/math-workshop-logo.png'
html_title = "SIO Math Workshop"

# Optional: customize theme options
html_theme_options = {
    "navbar_links": [
        {"href": "about", "text": "About"},
        {"href": "notebooks/example_notebook", "text": "Notebooks"},
        {"href": "https://github.com/USERNAME/REPO", "text": "GitHub"},
    ],
    "footer_links": [
        {"href": "about", "text": "About"},
        {"href": "notebooks/example_notebook", "text": "Notebooks"},
    ],
}

# Allow Markdown
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
