# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "videodb"
copyright = "2025, videodb"
author = "videodb"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys

sys.path.insert(0, os.path.abspath("../sdk_source"))  # Adjust path to SDK

# Output format
markdown_builder = {
    "output_format": "md",
}


extensions = [
    "sphinx.ext.autodoc",  # Extracts docstrings
    "sphinx.ext.napoleon",  # Google-style and NumPy-style docstrings
    "myst_parser",  # Allows Markdown support
    "sphinx_markdown_builder",  # Exports Markdown output
]


templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
