#!/bin/bash

cd rit
make clean
make html
find _build/html/ -name "*.html" -exec prettier --config ../json/.prettierrc.json --write {} +
cp -f ../js/copybutton-is.js _build/html/_static/copybutton.js