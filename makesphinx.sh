#!/bin/bash

cd rit
make clean
sphinx-build -b dirhtml . _build/html
find _build/html/ \( -name "*.html" -o -name "*.csss" \) -exec prettier --config .prettierrc --write {} +
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