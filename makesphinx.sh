#!/bin/bash

cd rit
make clean
sphinx-build -b dirhtml . _build/html
find _build/html/ -name "*.html" -exec prettier --config ../json/.prettierrc.json --write {} +
TARGET_FILE="_build/html/_static/copybutton.js"
SOURCE_FILE="../js/copybutton-is.js"
NEW_CODE=$(cat "$SOURCE_FILE")
sed -i '' "/const messages = {/r /dev/stdin" "$TARGET_FILE" << EOM
$NEW_CODE,
EOM
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