# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

projectid = 'Ritsafn-RÚBIK-Reykjavíkur--Öll-rit-sameinuð'   # Nafn á .tex og .pdf skrám í LaTeX
project = 'Ritsafn RÚBIK Reykjavíkur'                       # Nafn á titli á forsíðu í LaTeX og í seinni hlutanum í <title> í HTML

# Upplýsingar fyrir undirtitil í LaTeX
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

# Upplýsingar fyrir höfunda í LaTeX
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

# Upplýsingar fyrir höfundarrétt í LaTeX
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

# Notaðar viðbætur
extensions = [
    'sphinx_togglebutton',
    'sphinxcontrib.tikz',
]
root_doc = 'index'                                          # Aðal skrá verkefnis
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']     # Útiloka þessar skrár
templates_path = ['_templates']                             # Slóð á "templates" skrár
numfig = True                                               # Virkja tölusetningu (todo numfig)

# Snið fyrir tölusetningu (todo numfig)
numfig_format = {
    'figure': 'Mynd %s',
    'table': 'Tafla %s',
    'code-block': 'Kóða bálkur %s',
    'section': 'Grein %s'
}





# -- Options for internationalization ----------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-internationalization

language = 'is'     # Skráð <html lang="is" ...> í HTML og íslenska notuð þar sem það á við





# -- Options for Math --------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-math

math_number_all = True                      # Tölusetning virkjuð fyrir allar jöfnur (todo numfig)
math_eqref_format = 'Jafna.{number}'        # Snið fyrir tölusetningu fyrir jöfnur (todo numfig)
math_numfig = True                          # Tölusetning virkjuð fyrir jöfnur (todo numfig)





# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'              # Setur <html lang="is" ...> í HTML og notar íslensku þar sem það á við
html_theme_options = {
    "use_edit_page_button": True,               # "Edit on GitHub" takkinn virkjaður
    "search_bar_text": "Leita...",              # Þegar smellt er á "Leit", þá kemur upp gluggi með þessum texta
    "navbar_align": "content",                  # "navbar" er left-aligned frá þeim stað sem "content" byrjar
#    "header_links_before_dropdown": 1,          # Ákveða hversu margar síður birtast í header áður en að "More" takkinn kemur í staðinn
#    "announcement": "My announcement!",         # Tilkynning efst á síðunni

    # Icon og tenglar inn á samfélagsmiðla
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
html_title = project                            # Seinni hlutinn í <title> í HTML sóttur úr "project"
html_short_title = 'Ritsafn'                    # Stuttur title notaður í tenglum í "header" og í HTML Help Docs

# Skilgreiningar í HTML (t.d. fyrir tengil í "Edit on GitHub" takkanum)
html_context = {
    "github_user": "rubikrvk",
    "github_repo": "rubiktest",
    "github_version": "main",
}
html_css_files = ['custom.css']                 # Slóð á CSS skrár
html_static_path = ['_static']                  # Slóð á "static" skrár
html_show_copyright = False                     # Slökkt á default texta um höfundarrétt í HTML
html_show_sphinx = False                        # Slökkt á "Created using Sphinx" texta í HTML





# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

# Fall til setja undirtitil, höfunda og höfundarrétt inn í "author" (birtast bara á forsíðu)
def generate_info(info_list):

    # Búa til lista til að geyma upplýsingar
    info_lines = []
    for info in info_list:

        # Athuga hvort 'textnormal' sé til staðar og búa til línu í samræmi við það
        if info['textnormal']:
            line = r'\{}{{\textnormal{{{}}}}}'.format(info['size'], info['name'])
        else:
            line = r'\{}{{{}}}'.format(info['size'], info['name'])

        # Athuga hvort 'spacing' sé til staðar og bæta við línubili í samræmi við það
        if 'spacing' in info:
            line += r'\\[{}]'.format(info['spacing'])
        else:
            line += r'\\'

        # Bæta línunni við lista yfir upplýsingar
        info_lines.append(line)

    # Skila upplýsingunum sem streng með \newlineauthors skipuninni
    return r'\newlineauthors{{{}}}'.format(r' '.join(info_lines))

latex_subtitle = generate_info(subtitle)                                # Búa til LaTeX texta fyrir undirtitil
latex_authors = generate_info(authors)                                  # Búa til LaTeX texta fyrir höfunda
latex_copyright = generate_info(copyright)                              # Búa til LaTeX texta fyrir höfundarrétt
info = f'{latex_subtitle}\\\\ {latex_authors}\\\\ {latex_copyright}'    # Sameina upplýsingar í einn streng

latex_engine = 'pdflatex'          # latex_engine valin 
latex_documents = [
    ('index',                      # Upphafsskrá verkefnisins
     f'{projectid}.tex',           # Nafn á LaTeX skrá, byggt á projectid
     project,                      # Heiti verkefnisins
     info,                         # Undirtitill, höfundar og höfundarréttur sett inn í "author"
     'manual'),                    # LaTeX theme valið
]
latex_logo = '_static/rubik-cover.png'                              # Mynd á forsíðu
latex_toplevel_sectioning = 'part'                                  # toplevel_sectioning skráð sem Hluti (part)
latex_use_xindy = True                                              # Nota xindy í staðinn fyrir makeindex til að gera index fyrir general terms (from index usage) (todo)
latex_elements = {
    'papersize': 'a4paper',                                         # Nota A4 í staðinn fyrir default Letter
    'babel': '\\usepackage[icelandic]{babel}',                      # Nota íslensku fyrir hluta, kafla, efnisyfirlit, o.s.frv.
    'fontpkg': '\\usepackage{lmodern}\n\\usepackage[T1]{fontenc}',  # Setja allt letur í Latin modern
    'preamble': r'''

    % Koma í veg fyrir að kaflar byrji á oddatölusíðum
        \let\cleardoublepage\clearpage

    % Sérsniðin skipun til að meðhöndla línubil í höfunda hlutanum á forsíðu
        \newcommand{\newlineauthors}[1]{\parbox{0.8\textwidth}{\raggedleft#1}}

    % Fjarlægja dagsetningu af forsíðu
        \AtBeginDocument{\date{}}

    % Skilgreina litinn Blue Nova Deep
        \definecolor{bluenovadeep}{rgb}{0.192,0.255,0.604}

    % Skrá stillingar fyrir "hypersetup"
        \hypersetup{
            bookmarksnumbered=true,     % Kaflanúmer koma fram í Bookmarks
            bookmarksopen=true,         % Bookmarks eru alltaf opin 
            bookmarksopenlevel=1        % Bookmarks eru alltaf opin upp a level 1
            colorlinks=true,            % Tenglar birtast með litum
            linkcolor=black,            % "linkcolor" er svartur og inniheldur liti á tenglum í efnisyfirliti
            urlcolor=bluenovadeep,      % "urlcolor" er Blue Nova Deep og inniheldur liti á tenglum á forsíðu og inline tenglum
            citecolor=black,            % "citecolor" er svartur og inniheldur líklega liti á tenglum í genindex, o.fl. (todo)
        }

    % Skrá stillingar fyrir "titlesec" (notað hér til að velja liti á fyrirsögnum)
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