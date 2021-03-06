# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'JDFT'
copyright = '2022, SEA AI LAB'
author = 'Tianbo Li'

release = '0.0'
version = '0.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_book_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- customize theme color

html_theme_options = {
    # 'style_nav_header_background': '#910f0f',
    'show_toc_level': 2,
}

