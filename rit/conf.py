# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

projectid = 'RUBIK-oll-rit-sameinud'    # Nafn á .tex og .pdf skrám í LaTeX (verður að vera 'RUBIK-oll-rit-sameinud' fyrir "Sækja PDF" takkann)
project = 'Ritsafn RÚBIK Reykjavíkur'   # Nafn á titli á forsíðu í LaTeX og í seinni hlutanum í <title> í HTML

# Upplýsingar fyrir undirtitil í LaTeX
subtitle = [
    {
        'name': '~',
        'size': 'large',
        'spacing': '5em',
        'styles': []
    },
    {
        'name': 'Öll rit sameinuð (\href{https://rit.rubik.is}{rit.rubik.is})',
        'size': 'Large',
        'spacing': '1em',
        'styles': []
    },
]

# Upplýsingar fyrir höfunda í LaTeX
authors = [
    {
        'name': 'Eigandi efnis og leyfisveitandi:',
        'size': 'normalsize',
        'spacing': '0cm',
        'styles': ['textsf', 'textmd']
    },
    {
        'name': 'RÚBIK Reykjavík ehf. (\href{mailto:rubik@rubik.is}{rubik@rubik.is})',
        'size': 'large',
        'spacing': '1em',
        'styles': ['textsf', 'textmd']
    },
    {
        'name': 'Höfundur efnis:',
        'size': 'normalsize',
        'spacing': '0cm',
        'styles': ['textsf', 'textmd']
    },
    {
        'name': 'Atli Bjarnason (\href{mailto:rubik@rubik.is}{a@rubik.is})',
        'size': 'large',
        'spacing': '16em',
        'styles': ['textsf', 'textmd']
    },
]

# Upplýsingar fyrir höfundarrétt í LaTeX
copyright = [
    {
        'name': 'Ritsafn RÚBIK Reykjavíkur © 2023--\currentyear\ RÚBIK Reykjavík ehf.',
        'size': 'normalsize',
        'spacing': '0.3em',
        'styles': []
    },
    {
        'name': 'Notkun efnis úr Ritsafni RÚBIK Reykjavíkur er heimil samkvæmt \href{https://github.com/rubikrvk/ritsafn/blob/main/LICENSE}{notkunarleyfi} Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (\href{https://creativecommons.org/licenses/by-nc-sa/4.0/deed.is}{CC BY-NC-SA 4.0}).',
        'size': 'small',
        'spacing': '0em',
        'styles': ['textsf', 'textmd']
    },
]

# Leiðbeiningar fyrir 'size':
# ===========================
#
# \tiny         % Smallest font size
# \scriptsize   % Smaller than footnotesize
# \footnotesize % Small font size for footnotes
# \small        % Smaller than normalsize
# \normalsize   % Standard font size (default)
# \large        % Larger than normalsize
# \Large        % Larger than \large
# \LARGE        % Larger than \Large
# \huge         % Larger than \LARGE
# \Huge         % Largest font size
#
#
# Leiðbeiningar fyrir 'spacing':
# ==============================
#
# cm   % Centimeters
# mm   % Millimeters
# in   % Inches
# pt   % Points (1/72.27 inch)
# bp   % Big points (1/72 inch)
# pc   % Picas (1 pc = 12 pt)
# dd   % Didot points (1157 dd = 1238 pt)
# cc   % Ciceros (1 cc = 12 dd)
# sp   % Scaled points (65536 sp = 1 pt)
# em   % Width of the letter 'M' in the current font
# ex   % Height of the letter 'x' in the current font
# mu   % Math units (1/18 em, for mathematical spacing)
#
#
# Leiðbeiningar fyrir 'styles':
# =============================
#
#  'styles': ['textnormal']						% serif normal
#  'styles': ['textit', 'textnormal']			% serif normal italic
#  'styles': ['textrm']							% serif normal bold
#  'styles': ['textrm', 'textit']				% serif normal bold italic
#
#  'styles': ['textsf', 'textmd']				% sans serif normal
#  'styles': ['textsf', 'textmd', 'textit']		% serif normal italic
#  'styles': ['textsf']							% serif normal bold
#  'styles': ['textsf', 'textit']				% serif normal bold italic
#
#  'styles': ['texttt', 'textmd']				% mono normal
#  'styles': ['texttt', 'textmd', 'textit']		% mono normal italic
#  'styles': ['texttt']							% mono bold
#  'styles': ['texttt', 'textit']				% mono bold italic





# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Notaðar viðbætur
extensions = [
    'sphinxcontrib.tikz',
    'sphinx_sitemap',                                       # Búa til sitemap.xml skrá
    'sphinx_favicon',                                       # Setja inn favicon tengla og stillingar fyrir Progressive Web App (PWA) í <head>
    'sphinx_copybutton',                                    # Takki til að taka afrit af kóðablokkum
]

root_doc = 'index'                                          # Aðal skrá verkefnis

# Skrár sem á að útiloka í "build-*.sh"
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']     # Útiloka þetta alltaf
tags = globals().get('tags')                                # Sækja "tags" úr globals() ef það er til staðar, annars skilgreina sem "None" (tags = None)
if tags and 'dev' not in tags:                              # Athuga hvort "tags" sé ekki "None", og hvort það sé ekki "dev"
    exclude_patterns.append('eldhusvaskur/*')               # Útiloka þetta, nema "-t dev" sé notað í "build-*.sh"
#    exclude_patterns.append('mappa/*')                      # Útiloka þetta, nema "-t dev" sé notað í "build-*.sh"

templates_path = ['_templates']                             # Slóð á "templates" skrár
suppress_warnings = ['toc.excluded']                        # Slökkva á viðvörunum um að skrár (t.d. í "exclude_patterns") séu ennþá í toctree
numfig = True                                               # Sjálfvirk tölusetning í HTML á figures, tables og code-blocks
numfig_format = {
    'figure': 'Mynd %s',                                    # Snið fyrir tölusetningu mynda
    'table': 'Tafla %s',                                    # Snið fyrir tölusetningu taflna
    'code-block': 'Kóðablokk %s',                           # Snið fyrir tölusetningu kóðablokka
}
numfig_secnum_depth = 1                                     # Dýpt á sjálfvirkri tölusetningu í HTML // 0 = tölusetning er frá 1 upp í n // 1 = tölusetning er frá x.1 upp í x.n // 2 = tölusetning er frá x.y.1 upp í x.y.n // o.s.frv.

# Föll til að bæta við mismunandi numfig og numfig_secnum_depth í HTML annars vegar og í LaTeX hins vegar
def setup(app):
    # Bæta við numfig og numfig_secnum_depth í HTML sem default
    if 'numfig' not in app.config.values:
        app.add_config_value('numfig', numfig, 'env')
    if 'numfig_secnum_depth' not in app.config.values:
        app.add_config_value('numfig_secnum_depth', numfig_secnum_depth, 'env')
    
    def update_config_values(app):
        if app.builder.name in ['latex', 'latexpdf']:
            app.config.numfig = True                        # Sjálfvirk tölusetning í LaTeX á figures, tables og code-blocks
            app.config.numfig_secnum_depth = 2              # Dýpt á sjálfvirkri tölusetning í LaTeX // 0 = tölusetning er frá 1 upp í n // 1 = tölusetning er frá x.1 upp í x.n // 2 = tölusetning er frá x.y.1 upp í x.y.n // o.s.frv.
    
    # Bæta við numfig og numfig_secnum_depth í LaTeX
    app.connect('builder-inited', update_config_values)





# -- Options for internationalization ----------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-internationalization

language = 'is'                 # Skráð <html lang="is" ...> í HTML og íslenska notuð þar sem það á við
locale_dirs = ['_locale']       # Sækja þýðingar fyrir "is" í þessari möppu





# -- Options for Math --------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-math

math_eqref_format = '({number})'                # Snið fyrir tölusetningu fyrir jöfnur





# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'                          # Velja theme
html_theme_options = {
    "logo": {
        "alt_text": "Ritsafn RÚBIK Reykjavíkur",            # Alt texti fyrir logo
        "text": "Ritsafn RÚBIK Reykjavíkur",                # Texti við hliðina á logo
        "image_light": "_static/rubik-logo-light.svg",      # Logo fyrir light-mode
        "image_dark": "_static/rubik-logo-dark.svg",        # Logo fyrir dark-mode
    },
    "use_edit_page_button": True,                           # "Edit on GitHub" takkinn virkjaður
    "search_bar_text": "Sláðu inn leitarorð...",            # Þegar smellt er á "Leit" takkan, þá sést þessi texti í leitarglugga
    "navbar_align": "content",                              # "navbar" er left-aligned frá þeim stað sem "content" byrjar
    "navigation_depth": 5,                                  # Toc dýpt í left sidebar
    "show_toc_level": 5,                                    # Toc dýpt í right sidebar
    "header_links_before_dropdown": 2,                      # Hversu margar síður birtast í header áður en að "More" takkinn tekur við
    "header_dropdown_text": "Meira",                        # Íslenskur texti fyrir "More" takkann
    "back_to_top_button": False,                            # Fjarlægja "Efst á síðu" takkann
    #"announcement": "My announcement!",                     # Tilkynning efst á síðunni

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
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/company/rubikrvk",
            "icon": "fa-brands fa-linkedin",
        },
        {
            "name": "TikTok",
            "url": "https://tiktok.com/@rubikrvk",
            "icon": "fa-brands fa-tiktok",
        },
        {
            "name": "YouTube",
            "url": "https://www.youtube.com/@rubikrvk",
            "icon": "fa-brands fa-youtube",
        },
        {
            "name": "Threads",
            "url": "https://www.threads.net/@rubikrvk",
            "icon": "fa-brands fa-threads",
        },
    ],
    "secondary_sidebar_items": {
        "**": ["rubik-page-toc", "rubik-pdf", "rubik-sourcelink", "rubik-edit-this-page"],      # LAYOUT - Sýna þetta á öllum síðum
        "genindex": [],                                                                         # LAYOUT - Tómt í genindex
        "search": [],                                                                           # LAYOUT - Tómt í search
    },
    "show_prev_next": False,                                                                    # Ekki sýna "fyrri síða" og "næsta síða" takka neðst í content
    "article_header_start": [],                                                                 # LAYOUT - Hér er hægt að hafa t.d. breadcrumbs
    "footer_end": [],                                                                           # LAYOUT
    "navbar_end": ["theme-switcher"],                                                           # LAYOUT
    "navbar_persistent": ["search-button-field"],                                               # LAYOUT - Þetta fer ekki inn í primary sidebar á mobile
    "footer_start": ["rubik-copyright"],                                                        # LAYOUT
}
html_baseurl = 'https://rit.rubik.is/'                                                          # Notað í URLs í sitemap.xml
html_context = {
    "github_version": "main",                                                                   # Skilgreining fyrir tengil í "Edit on GitHub" takkanum
    "github_user": "rubikrvk",                                                                  # Skilgreining fyrir tengil í "Edit on GitHub" takkanum
    "github_repo": "ritsafn",                                                                   # Skilgreining fyrir tengil í "Edit on GitHub" takkanum
    "doc_path": "rit",                                                                          # Skilgreining fyrir tengil í "Edit on GitHub" takkanum
}
html_css_files = ['custom.css']                                                                 # Slóð á CSS skrár
html_static_path = ['_static']                                                                  # Slóð á "static" skrár
html_sidebars = {
    "**": ["rubik-sidebar-nav-section", "rubik-icon-links"],                                    # LAYOUT - Sýna þetta á öllum síðum
    "index": ["rubik-sidebar-nav-root", "rubik-icon-links"],                                    # LAYOUT - Sýna fyrirsögnina "Yfirlit" í index
    "search": ["rubik-sidebar-nav-root", "rubik-icon-links"],                                   # LAYOUT - Sýna fyrirsögnina "Yfirlit" í search
}
html_show_copyright = False                                                                     # Slökkt á default texta um höfundarrétt í HTML
html_show_sphinx = False                                                                        # Slökkt á "Created using Sphinx" texta í HTML





# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

# Föll til að setja undirtitil, höfunda og höfundarrétt inn í "author" (birtast bara á forsíðu, og reyndar líka inn í "author description" inn í PDF properties)
def generate_info(info_list):
    def apply_styles(text, styles):
        if not styles:
            return text
        styled_text = text
        for style in styles:
            styled_text = r'\{}{{{}}}'.format(style, styled_text)
        return styled_text

    info_lines = []
    for info in info_list:
        styled_name = apply_styles(info['name'], info.get('styles', []))
        line = r'\{}{{{}}}'.format(info['size'], styled_name)

        if 'spacing' in info:
            line += r'\\[{}]'.format(info['spacing'])
        else:
            line += r'\\'

        info_lines.append(line)

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
latex_use_xindy = False                                             # Nota xindy í staðinn fyrir makeindex til að gera index fyrir general terms (from index usage) (todo)
latex_elements = {
    'papersize': 'a4paper',                                         # Nota A4 í staðinn fyrir default Letter
    'babel': '\\usepackage[icelandic]{babel}',                      # Nota íslensku fyrir hluta, kafla, efnisyfirlit, o.s.frv.
    'fontpkg': '\\usepackage{lmodern}\n\\usepackage[T1]{fontenc}',  # Setja allt letur í Latin modern
    'preamble': r'''

    % Koma í veg fyrir að kaflar byrji á oddatölusíðum
        \let\cleardoublepage\clearpage

    % Sérsniðin skipun til að meðhöndla línubil í höfunda hlutanum á forsíðu
        \newcommand{\newlineauthors}[1]{\parbox{0.8\textwidth}{\raggedleft#1}}

    % Skilgreina "currentyear" sem núverandi ár
        \newcommand{\currentyear}{\the\year}

    % Fjarlægja dagsetningu af forsíðu
        \AtBeginDocument{\date{}}

    % Skilgreina litinn Blue Nova Deep
        \definecolor{bluenovadeep}{rgb}{0.192,0.255,0.604}

    % Skrá stillingar fyrir "hypersetup"
        \hypersetup{
            bookmarksnumbered=true,     % Kaflanúmer koma fram í Bookmarks
            bookmarksopen=true,         % Bookmarks eru alltaf opin
            bookmarksopenlevel=0,       % Bookmarks eru alltaf opin upp að kafla (en ekki undirkafla)
            pdfnewwindow=true,          % Tenglar opnast í nýjum glugga í vafra (virkar samt ekki í öllum vöfrum)
            colorlinks=true,            % Tenglar birtast með litum
            linkcolor=black,            % "linkcolor" er svartur og inniheldur liti á tenglum í efnisyfirliti
            urlcolor=bluenovadeep,      % "urlcolor" er Blue Nova Deep og inniheldur liti á tenglum á forsíðu og inline tenglum
            citecolor=black,            % "citecolor" er svartur og inniheldur líklega liti á tilvísunum úr t.d. bibtex, o.fl. (todo)
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

    % Skrá " endash " í staðinn fyrir ": " á milli numfig_format og caption, og gera numfig_format bold
        \usepackage{caption}
        \captionsetup{labelsep=endash, labelfont={bf}}
    '''
}





# -- MathJax configuration ---------------------------------------------------

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"

mathjax3_config = {
    "tex": {
        "inlineMath": [["$", "$"], ["\\(", "\\)"]],
        "processEscapes": True,
    },
    "options": {
        "ignoreHtmlClass": "tex2jax_ignore|mathjax_ignore|document",
        "processHtmlClass": "tex2jax_process|mathjax_process|math|output_area",
    },
    "svg": {
        "fontCache": "global",
        "mtextInheritFont": True,
        "scale": 1,
    },
}





# -- sphinxcontrib.tikz configuration ----------------------------------------

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





# -- sphinx_sitemap configuration --------------------------------------------

sitemap_url_scheme = "{link}"                               # Fjarlægja "/is" hlutann úr URLs í sitemap.xml





# -- sphinx_favicon configuration --------------------------------------------

favicons = [ # Sbr. https://dev.to/masakudamatsu/favicon-nightmare-how-to-maintain-sanity-3al7
    {"rel": "icon", "href": "https://rit.rubik.is/_static/favicon/favicon.ico", "sizes": "48x48"},      # Fyrir Safari og gamla IE vafra
    {"rel": "icon", "href": "https://rit.rubik.is/_static/favicon/icon.svg", "sizes": "any"},           # Fyrir flesta aðra vafra
    {"rel": "apple-touch-icon", "href": "https://rit.rubik.is/_static/favicon/apple-touch-icon.png"},   # Fyrir "Add to Home Screen" í Apple tækjum
    {"rel": "manifest", "href": "https://rit.rubik.is/_static/site.webmanifest"},                       # JSON skrá fyrir "Home Screen icon" á Android tækjum og með stillingum fyrir Progressive Web App (PWA)
]





# -- Sækja PDF configuration -------------------------------------------------

# Föll fyrir "Sækja PDF" takkann
def add_data_attributes(app, pagename, templatename, context, doctree):

    # Reikna fjölda skráarstiga í slóðinni
    depth = pagename.count('/')
    
    # Ákvarða nafn undirmöppu ef hún er til staðar
    if depth >= 1:
        subfolder = pagename.split('/')[0]
    else:
        subfolder = ''
    
    # Prenta upplýsingar um núverandi síðu, dýpt og undirmöppu (fyrir villuleit)
    print(f"Processing page: {pagename}, Depth: {depth}, Subfolder: {subfolder}")
    
    # Bæta dýpt og nafni undirmöppu við samhengi (context) sem breytur
    context['html_page_depth'] = depth
    context['html_subfolder'] = subfolder

def setup(app):

    # Tengja add_data_attributes fallið við 'html-page-context' atburðinn í Sphinx
    app.connect('html-page-context', add_data_attributes)



