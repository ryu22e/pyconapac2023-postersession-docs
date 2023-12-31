# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Python Boot Campの紹介 - あなたの街で開催しませんか?'
copyright = '2023, Ryuji Tsutsui'
author = 'Ryuji Tsutsui'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinxcontrib.mermaid',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_extra_path = [
    "robots.txt",
]

locale_dirs = ['locale/']
gettext_compact = False

html_css_files = ['custom.css']

mermaid_cmd = './node_modules/.bin/mmdc'
mermaid_output_format = 'svg'
