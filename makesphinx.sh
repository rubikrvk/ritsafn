#!/bin/bash

cd rit
make clean
sphinx-build -b dirhtml . _build/html
find _build/html/ -name "*.html" -exec prettier --config ../json/.prettierrc.json --write {} +
TARGET_FILE="_build/html/_static/copybutton.js"
SOURCE_FILE="../js/copybutton-is.js"
NEW_CODE=$(cat "$SOURCE_FILE")

# Create a temporary file to hold the modified content
TEMP_FILE=$(mktemp)

# Insert NEW_CODE after the line containing 'const messages = {'
awk -v new_code="$NEW_CODE" '
    {print}
    /const messages = {/ {
        print new_code ","
    }
' "$TARGET_FILE" > "$TEMP_FILE"

# Replace the original file with the modified file
mv "$TEMP_FILE" "$TARGET_FILE"

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