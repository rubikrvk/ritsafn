#!/bin/bash

cd rit
make clean
make html
find _build/html/ -name "*.html" -exec prettier --config ../json/.prettierrc.json --write {} +
cp -f ../js/copybutton.js _build/html/_static/
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