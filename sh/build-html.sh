#!/bin/bash

cd rit
make clean
make html
find _build/html/ -name "*.html" -exec prettier --config ../json/.prettierrc.json --write {} +
cp -f ../js/copybutton.js _build/html/_static/