# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ritsafn RÚBIK Reykjavíkur'
copyright = '2024, RÚBIK Reykjavík ehf'
author = 'RÚBIK Reykjavík ehf'
release = '2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'is'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = project
html_static_path = ['_static']
html_theme = 'sphinx_book_theme'
html_theme_options = {
    "use_edit_page_button": True,
    "use_source_button": True,
    "use_download_button": True,
    "search_bar_text": "Leita...",
    "announcement": "My announcement!",
    "max_navbar_depth": 6,
    "collapse_navbar": True,
    "toc_title": "Smá test TOC titill",
}
html_context = {
    # "github_url": "https://github.com/rubikrvk/rubiktest", # or your GitHub Enterprise site
    "github_user": "rubikrvk",
    "github_repo": "rubiktest",
    "github_version": "main",
    "doc_path": "docs/source/",
}

# -- Options for LaTeX output ------------------------------------------------
latex_engine = 'pdflatex'
latex_theme = 'manual'
latex_elements = {
    'babel': '\\usepackage[icelandic]{babel}',
    'papersize': 'a4paper',
    'fontpkg': '\\usepackage{lmodern}\n\\usepackage[T1]{fontenc}',
}
#latex_documents = [
#    ('index', 'YourProject.tex', project, author, latex_theme),
#]

latex_toplevel_sectioning = 'part'
