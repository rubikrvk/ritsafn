# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ritsafn RÚBIK Reykjavíkur'
author = 'RÚBIK Reykjavík ehf'





# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_togglebutton',
    'sphinxcontrib.tikz',
]
root_doc = 'index'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
templates_path = ['_templates']
numfig = True
numfig_format = {
    'figure': 'Mynd %s',
    'table': 'Tafla %s',
    'code-block': 'Kóða bálkur %s',
    'section': 'Grein %s'
}





# -- Options for internationalization ----------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-internationalization

language = 'is'





# -- Options for Math --------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-math

math_number_all = True
math_eqref_format = 'Jafna.{number}'
math_numfig = True





# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    "use_edit_page_button": True,
    "search_bar_text": "Leita...",
    "navbar_align": "content",
#    "header_links_before_dropdown": 1, #Ákveða hversu margar síður birtast í header áður en að "More" takkinn kemur í staðinn
#    "announcement": "My announcement!", #Tilkynning efst á síðunni
    "icon_links": [
        {
            "name": "Facebook",
            "url": "https://facebook.com/rubikrvk",
            "icon": "fa-brands fa-facebook",
        },
        {
            "name": "Instagram",
            "url": "https://instagram.com/rubikrvk",
            "icon": "fa-brands fa-instagram",
        },
        {
            "name": "X.com",
            "url": "https://x.com/rubikrvk",
            "icon": "fa-brands fa-x-twitter",
        },
        {
            "name": "YouTube",
            "url": "https://www.youtube.com/@rubikrvk",
            "icon": "fa-brands fa-youtube",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/company/rubikrvk",
            "icon": "fa-brands fa-linkedin",
        },    ]
}
html_title = project
html_short_title = 'Ritsafn'
html_context = {
    "github_user": "rubikrvk",
    "github_repo": "rubiktest",
    "github_version": "main",
}
html_css_files = ['custom.css']
html_static_path = ['_static']
html_show_copyright = False
html_show_sphinx = False





# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_engine = 'pdflatex'
#latex_documents = [
#    ('index', 'YourProject.tex', project, author, latex_theme),
#]
#latex_logo = ''
latex_toplevel_sectioning = 'part'
latex_show_urls = 'footnote'
latex_use_xindy = True
latex_elements = {
    'babel': '\\usepackage[icelandic]{babel}',
    'papersize': 'a4paper',
    'fontpkg': '\\usepackage{lmodern}\n\\usepackage[T1]{fontenc}',
}
latex_theme = 'manual'





# -- MathJax configuration ---------------------------------------------------

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"

mathjax3_config = {
    "loader": {
        "load": ["[tex]/noerrors", "[tex]/noundefined"]
    },
    "tex": {
        "inlineMath": [["$", "$"], ["\\(", "\\)"]],
        "displayMath": [["$$", "$$"], ["\\[", "\\]"]],
        "packages": {"[+]": ["noerrors", "noundefined"]}
    },
    "svg": {
        "fontCache": "global",
        "matchVerticalAlign": False,
        "mtextInheritFont": False,
        "scale": 1,
    }
}





# -- sphinxcontrib-tikz configuration ----------------------------------------

tikz_proc_suite = 'pdf2svg'
tikz_latex_preamble = r"""
\usepackage{transparent}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{array}
\usepackage{ragged2e}
\usepackage{graphicx}
\usepackage{pgfplots}
\usepackage{pgfplotstable}
\usepackage{multirow}
\usepackage{booktabs}
\pgfplotsset{compat=1.18, plot coordinates/math parser=false}
\usepackage{amsmath, amsfonts, amssymb}
\usepackage{xcolor}
\usepackage{geometry}
\usepgfplotslibrary{patchplots, polar, fillbetween, ternary}
\usetikzlibrary{arrows.meta, patterns, plotmarks, shapes.geometric, decorations.pathmorphing, decorations.text, graphs, positioning, calc, 3d}
\geometry{a4paper, margin=1in}
\usepackage{hyperref}
"""
tikz_output_format = 'svg'
tikz_tikzlibraries = 'pgfplots.groupplots'
tikz_externalize = True
tikz_latex_args = [r"-shell-escape"]