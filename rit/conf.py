# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

projectid = 'Ritsafn-RÚBIK-Reykjavíkur--Öll-rit-sameinuð'
project = 'Ritsafn RÚBIK Reykjavíkur'
subtitle = [
    {
        'name': '~',
        'size': 'large',
        'spacing': '2cm',
        'textnormal': False
    },
    {
        'name': 'Öll rit sameinuð (\href{https://rit.rubik.is}{rit.rubik.is})',
        'size': 'Large',
        'spacing': '0.6cm',
        'textnormal': False
    },
]
authors = [
    {
        'name': 'Eigandi efnis og leyfisveitandi:',
        'size': 'normalsize',
        'spacing': '0cm',
        'textnormal': False
    },
    {
        'name': 'RÚBIK Reykjavík ehf. (\href{mailto:rubik@rubik.is}{rubik@rubik.is})',
        'size': 'large',
        'spacing': '0.5cm',
        'textnormal': True
    },
    {
        'name': 'Höfundur efnis:',
        'size': 'normalsize',
        'spacing': '0cm',
        'textnormal': False
    },
    {
        'name': 'Atli Bjarnason (\href{mailto:rubik@rubik.is}{a@rubik.is})',
        'size': 'large',
        'spacing': '7.5cm',
        'textnormal': True
    },
]
copyright = [
    {
        'name': 'Ritsafn RÚBIK Reykjavíkur © RÚBIK Reykjavík ehf.',
        'size': 'normalsize',
        'spacing': '0.2cm',
        'textnormal': False
    },
    {
        'name': 'Notkun efnis er heimil samkvæmt \href{https://github.com/rubikrvk/ritsafn/blob/main/LICENSE}{notkunarleyfi} Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (\href{https://creativecommons.org/licenses/by-nc-sa/4.0/deed.is}{CC BY-NC-SA 4.0}).',
        'size': 'normalsize',
        'spacing': '0.2cm',
        'textnormal': True
    },
]





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

def generate_info(info_list):
    info_lines = []
    for info in info_list:
        if info['textnormal']:
            line = r'\{}{{\textnormal{{{}}}}}'.format(info['size'], info['name'])
        else:
            line = r'\{}{{{}}}'.format(info['size'], info['name'])
        if 'spacing' in info:
            line += r'\\[{}]'.format(info['spacing'])
        else:
            line += r'\\'
        info_lines.append(line)
    return r'\newlineauthors{{{}}}'.format(r' '.join(info_lines))

latex_subtitle = generate_info(subtitle)
latex_authors = generate_info(authors)
latex_copyright = generate_info(copyright)
info = f'{latex_subtitle}\\\\ {latex_authors}\\\\ {latex_copyright}'

latex_engine = 'pdflatex'
latex_documents = [
    ('index', f'{projectid}.tex', project, info, 'manual'),
]
latex_logo = '_static/rubik-cover.png'
latex_toplevel_sectioning = 'part'
latex_use_xindy = True
latex_elements = {
    'papersize': 'a4paper',
    'babel': '\\usepackage[icelandic]{babel}',
    'fontpkg': '\\usepackage{lmodern}\n\\usepackage[T1]{fontenc}',
    'preamble': r'''

    % Prevent chapters from starting on odd pages
        \let\cleardoublepage\clearpage

    % Custom command to handle newlines in author field
        \newcommand{\newlineauthors}[1]{\parbox{0.8\textwidth}{\raggedleft#1}}

    % Remove date from Title page
        \AtBeginDocument{\date{}}

    % Define the Blue Nova Deep color
        \definecolor{bluenovadeep}{rgb}{0.192,0.255,0.604}

    % Set hyperlink color to Blue Nova Deep
        \hypersetup{
            colorlinks=true,
            linkcolor=black,        % Includes colors in TOC 
            urlcolor=bluenovadeep,  % Includes colors in Title page and inline links 
            citecolor=black,        % Probably includes links in genindex, etc.
        }

    % Set headings color to Black (also possible to use Blue Nova Deep)
        \usepackage{titlesec}
        \titleformat{\section}
            {\normalfont\Large\bfseries\color{black}}{\thesection}{1em}{\bfseries}
        \titleformat{\subsection}
            {\normalfont\large\bfseries\color{black}}{\thesubsection}{1em}{}
        \titleformat{\subsubsection}
            {\normalfont\normalsize\bfseries\color{black}}{\thesubsubsection}{1em}{}
        \titleformat{\paragraph}
            {\normalfont\normalsize\bfseries\color{black}}{\theparagraph}{1em}{}
        \titleformat{\subparagraph}
            {\normalfont\normalsize\bfseries\color{black}}{\thesubparagraph}{1em}{}
    '''
}





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