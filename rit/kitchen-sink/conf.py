import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from conf import *

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

projectid = 'Ritsafn-RÚBIK-Reykjavíkur--Kitchen-sink'   # UPPFÆRT - Nafn á .tex og .pdf skrám í LaTeX
project = 'Kitchen sink'                                # UPPFÆRT - Nafn á titli á forsíðu í LaTeX og í seinni hlutanum í <title> í HTML

# UPPFÆRT - Upplýsingar fyrir undirtitil í LaTeX
subtitle = [
    {
        'name': '~',
        'size': 'large',
        'spacing': '2cm',
        'textnormal': False
    },
    {
        'name': 'Ritsafn RÚBIK Reykjavíkur (\href{https://rit.rubik.is}{rit.rubik.is})',
        'size': 'Large',
        'spacing': '0.6cm',
        'textnormal': False
    },
]

# UPPFÆRT - Upplýsingar fyrir höfunda í LaTeX

# UPPFÆRT - Upplýsingar fyrir höfundarrétt í LaTeX





# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

# ÓBREYTT - Þarf samt að endurtaka hér fyrir fall
def generate_info(info_list):

    # ÓBREYTT - Þarf samt að endurtaka hér fyrir fall
    info_lines = []
    for info in info_list:

        # ÓBREYTT - Þarf samt að endurtaka hér fyrir fall
        if info['textnormal']:
            line = r'\{}{{\textnormal{{{}}}}}'.format(info['size'], info['name'])
        else:
            line = r'\{}{{{}}}'.format(info['size'], info['name'])

        # ÓBREYTT - Þarf samt að endurtaka hér fyrir fall
        if 'spacing' in info:
            line += r'\\[{}]'.format(info['spacing'])
        else:
            line += r'\\'

        # ÓBREYTT - Þarf samt að endurtaka hér fyrir fall
        info_lines.append(line)

    # ÓBREYTT - Þarf samt að endurtaka hér fyrir fall
    return r'\newlineauthors{{{}}}'.format(r' '.join(info_lines))

latex_subtitle = generate_info(subtitle)                                # ÓBREYTT - Þarf samt að endurtaka hér fyrir fall
latex_authors = generate_info(authors)                                  # ÓBREYTT - Þarf samt að endurtaka hér fyrir fall
latex_copyright = generate_info(copyright)                              # ÓBREYTT - Þarf samt að endurtaka hér fyrir fall
info = f'{latex_subtitle}\\\\ {latex_authors}\\\\ {latex_copyright}'    # ÓBREYTT - Þarf samt að endurtaka hér fyrir fall

latex_documents = [
    ('index',                      # ÓBREYTT - Þarf samt að endurtaka hér fyrir fall
     f'{projectid}.tex',           # ÓBREYTT - Þarf samt að endurtaka hér fyrir fall
     project,                      # ÓBREYTT - Þarf samt að endurtaka hér fyrir fall
     info,                         # ÓBREYTT - Þarf samt að endurtaka hér fyrir fall
     'manual'),                    # ÓBREYTT - Þarf samt að endurtaka hér fyrir fall
]
latex_logo = '../_static/rubik-cover.png'                           # UPPFÆRT - Mynd á forsíðu
latex_toplevel_sectioning = 'chapter'                               # UPPFÆRT - toplevel_sectioning skráð sem Kafli (chapter)