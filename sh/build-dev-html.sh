#!/bin/bash

# Búa til HTML skrár með "-b html -t dev" (sem lætur alla hlekki vísa á "<slóð>/<skrá>.html", en ekki á "<slóð>/" eins og "-b dirhtml" gerir)
cd rit
make clean
sphinx-build -b html -t dev . _build/html

# Keyra Prettier á allar HTML skrár
find _build/html/ -name "*.html" -exec prettier --config ../json/.prettierrc.json --write {} +

# Bæta við íslenskum þýðingum fyrir sphinx_copybutton
cp -f ../js/copybutton-is.js _build/html/_static/copybutton.js