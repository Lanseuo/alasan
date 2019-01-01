#!/usr/bin/env python3

from recommonmark.parser import CommonMarkParser
import guzzle_sphinx_theme
extensions = ["sphinx.ext.autodoc",
              "sphinx.ext.coverage",
              "sphinx_markdown_tables"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

source_suffix = [".rst", ".md"]
source_parsers = {".md": CommonMarkParser}

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Alasan"
copyright = "2019, Lucas Hild"
author = "Lucas Hild"

version = "0.0.1"
release = version

language = None
exclude_patterns = []
pygments_style = "sphinx"
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# htlm_theme = "alabaster"
html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes", ]
html_static_path = ["_static"]
htmlhelp_basename = "alasandoc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}
latex_documents = [
    (master_doc, "alasan.tex", "Alasan Documentation",
     "Lucas Hild", "manual"),
]

# -- Options for manual page output ---------------------------------------

man_pages = [
    (master_doc, "Alasan", "Alasan Documentation",
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
    (master_doc, "Alasan", "Alasan Documentation",
     author, "Alasan", "One line description of project.",
     "Miscellaneous"),
]
