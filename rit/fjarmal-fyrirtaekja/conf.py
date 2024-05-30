import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # Add parent directory to sys.path

from conf import *  # Import everything from the main conf.py

# Override specific settings for the Economics book
project = 'Ritsafn RÚBIK Reykjavíkur\nFjármál einstaklinga'
author = 'Author One\nAuthor Two'
latex_toplevel_sectioning = 'chapter'
html_static_path = ['../_static']

# Modify the LaTeX documents setting to use the custom commands for title and authors
latex_documents = [
    ('index', 'EconomicsBook.tex', r'\newlinetitle{Economics\\Book}', 
     r'\newlineauthors{Author One\\Author Two}', 'manual'),
]