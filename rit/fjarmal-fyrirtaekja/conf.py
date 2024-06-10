import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from conf import *

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

projectid = 'RUBIK-fjarmal-fyrirtaekja'     # UPPFÆRT - Nafn á .tex og .pdf skrám í LaTeX (verður að vera 'RUBIK-<nafn á undirmöppu>' fyrir "Sækja PDF" takkann)
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





# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

numfig = True                                               # ÓBREYTT - Þarf samt að endurtaka hér fyrir föll
numfig_secnum_depth = 1                                     # ÓBREYTT - Þarf samt að endurtaka hér fyrir föll

# ÓBREYTT - Þarf samt að endurtaka hér fyrir föll
def setup(app):
    # ÓBREYTT - Þarf samt að endurtaka hér fyrir föll
    if 'numfig' not in app.config.values:
        app.add_config_value('numfig', numfig, 'env')
    if 'numfig_secnum_depth' not in app.config.values:
        app.add_config_value('numfig_secnum_depth', numfig_secnum_depth, 'env')
    
    def update_config_values(app):
        if app.builder.name in ['latex', 'latexpdf']:
            app.config.numfig = True                        # UPPFÆRT - Sjálfvirk tölusetning í LaTeX á figures, tables og code-blocks
            app.config.numfig_secnum_depth = 1              # UPPFÆRT - Dýpt á sjálfvirkri tölusetning í LaTeX // 0 = tölusetning er frá 1 upp í n // 1 = tölusetning er frá x.1 upp í x.n // 2 = tölusetning er frá x.y.1 upp í x.y.n // o.s.frv.
    
    # ÓBREYTT - Þarf samt að endurtaka hér fyrir föll
    app.connect('builder-inited', update_config_values)





# -- Options for internationalization ----------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-internationalization

language = 'is'     # Skráð <html lang="is" ...> í HTML og íslenska notuð þar sem það á við
locale_dirs = ['../locale']





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