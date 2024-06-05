import os
from sphinx.application import Sphinx

def add_pdf_link(app, pagename, templatename, context, doctree):
    if templatename == 'rubik-pdf.html':
        build_dir = app.outdir
        parts = pagename.split('/')
        
        if len(parts) == 1:
            pdf_link = 'RUBIK-oll-rit-sameinud.pdf'
        else:
            subfolder = parts[0]
            pdf_link = f'RUBIK-{subfolder}.pdf'
        
        context['pdf_link'] = pdf_link

def setup(app: Sphinx):
    app.connect('html-page-context', add_pdf_link)
