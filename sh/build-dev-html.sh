#!/bin/bash

# Búa til HTML skrár með "-b html -t dev" (sem lætur alla hlekki vísa á "<slóð>/<skrá>.html", en ekki á "<slóð>/" eins og "-b dirhtml" gerir)
cd rit
make clean
sphinx-build -b html -t dev . _build/html

# Bæta "noindex, nofollow" við <head> í öllum HTML skrám
find _build/html/ -name '*.html' -exec sed -i '' -e 's/<head>/<head>\n<meta name="robots" content="noindex, nofollow">/' {} +

# Fjarlægja "type" úr <link rel="icon" href="/favicon.ico" ... > og <link rel="apple-touch-icon" href="/apple-touch-icon.png" ... >
find _build/html/ -name '*.html' -exec sed -i '' -e 's#<link rel="icon" href="_static/favicon/favicon.ico" sizes="32x32"[^>]*>#<link rel="icon" href="_static/favicon/favicon.ico" sizes="32x32">#' {} +
find _build/html/ -name '*.html' -exec sed -i '' -e 's#<link rel="apple-touch-icon" href="_static/favicon/apple-touch-icon.png"[^>]*>#<link rel="apple-touch-icon" href="_static/favicon/apple-touch-icon.png">#' {} +

# Keyra Prettier á allar HTML skrár
find _build/html/ -name "*.html" -exec prettier --config ../json/.prettierrc.json --write {} +

# Bæta við íslenskum þýðingum fyrir sphinx_copybutton
cp -f ../js/copybutton-is.js _build/html/_static/copybutton.js