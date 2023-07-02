# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'scbirlab.github.io'
copyright = '2023, SCBIRLab'
author = 'SCBIRLab'
release = '0.0.1'

master_doc = "index"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_design"
]

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

myst_heading_anchors = 2

templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_theme_options = {
    "repository_url": "https://github.com/scbirlab/scbirlab.github.io",
    "repository_branch": "master",
    "use_repository_button": True,
    "use_download_button": False,
    "use_fullscreen_button": False,
    "favicons": [
        {
         "rel": "icon",
         "sizes": "512x512",
         "href": "favicon.png",
      }
    ]
}

html_logo = "_static/lab-logo.png"
html_title = "SCBIRLab"

html_sidebars = {
    "**": ["navbar-logo.html", "sbt-sidebar-nav.html"]
}