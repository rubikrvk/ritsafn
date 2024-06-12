#!/bin/bash

cd rit
make clean
sphinx-build -b dirhtml . _build/html
find _build/html/ -name "*.html" -exec prettier --config ../json/.prettierrc.json --write {} +
cp -f ../js/copybutton-is.js _build/html/_static/copybutton.js
make latexpdf
mv _build/latex/*.pdf _build/html/
for dir in */ ; do
  if [[ -d "$dir" && "$dir" != _* ]]; then
    cd "$dir"
    make clean
    make latexpdf
    mv _build/latex/*.pdf "../_build/html/${dir%/}/"
    cd ..
  fi
done