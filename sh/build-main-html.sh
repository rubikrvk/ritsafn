#!/bin/bash

# Búa til HTML skrár með "-b html" (sem lætur alla hlekki vísa á "<slóð>/<skrá>.html", en ekki á "<slóð>/" eins og "-b dirhtml" gerir)
cd rit
make clean
sphinx-build -b html . _build/html

# Fjarlægja "type" úr <link rel="icon" href="/favicon.ico" ... > og <link rel="apple-touch-icon" href="/apple-touch-icon.png" ... >
find _build/html/ -name '*.html' -exec sed -i '' -e 's#<link rel="icon" href="/favicon.ico" sizes="32x32" type="image/x-icon" />#<link rel="icon" href="/favicon.ico" sizes="32x32">#' {} +
find _build/html/ -name '*.html' -exec sed -i '' -e 's#<link rel="apple-touch-icon" href="/apple-touch-icon.png" type="image/png" />#<link rel="apple-touch-icon" href="/apple-touch-icon.png">#' {} +

# Keyra Prettier á allar HTML skrár
find _build/html/ -name "*.html" -exec prettier --config ../json/.prettierrc.json --write {} +

# Bæta við íslenskum þýðingum fyrir sphinx_copybutton
cp -f ../js/copybutton-is.js _build/html/_static/copybutton.js