import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from conf import *

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

projectid = 'RUBIK-fjarmal-fyrirtaekja'     # UPPFÆRT - Nafn á .tex og .pdf skrám í LaTeX
project = 'Fjármál fyrirtækja'              # UPPFÆRT - Nafn á titli á forsíðu í LaTeX og í seinni hlutanum í <title> í HTML

# UPPFÆRT - Upplýsingar fyrir undirtitil í LaTeX
subtitle = [
    {
        'name': '~',
        'size': 'large',
        'spacing': '5em',
        'styles': []
    },
    {
        'name': 'Ritsafn RÚBIK Reykjavíkur (\href{https://rit.rubik.is}{rit.rubik.is})',
        'size': 'Large',
        'spacing': '1em',
        'styles': []
    },
]

# UPPFÆRT - Upplýsingar fyrir höfunda í LaTeX

# UPPFÆRT - Upplýsingar fyrir höfundarrétt í LaTeX





# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['../_static']               # UPPFÆRT - Slóð á "static" skrár





# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

# ÓBREYTT - Þarf samt að endurtaka hér fyrir föll
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

latex_subtitle = generate_info(subtitle)                                # ÓBREYTT - Þarf samt að endurtaka hér fyrir föll
latex_authors = generate_info(authors)                                  # ÓBREYTT - Þarf samt að endurtaka hér fyrir föll
latex_copyright = generate_info(copyright)                              # ÓBREYTT - Þarf samt að endurtaka hér fyrir föll
info = f'{latex_subtitle}\\\\ {latex_authors}\\\\ {latex_copyright}'    # ÓBREYTT - Þarf samt að endurtaka hér fyrir föll

latex_documents = [
    ('index',                      # ÓBREYTT - Þarf samt að endurtaka hér fyrir föll
     f'{projectid}.tex',           # ÓBREYTT - Þarf samt að endurtaka hér fyrir föll
     project,                      # ÓBREYTT - Þarf samt að endurtaka hér fyrir föll
     info,                         # ÓBREYTT - Þarf samt að endurtaka hér fyrir föll
     'manual'),                    # ÓBREYTT - Þarf samt að endurtaka hér fyrir föll
]
latex_logo = '../_static/rubik-cover.png'                           # UPPFÆRT - Mynd á forsíðu
latex_toplevel_sectioning = 'chapter'                               # UPPFÆRT - toplevel_sectioning skráð sem Kafli (chapter)