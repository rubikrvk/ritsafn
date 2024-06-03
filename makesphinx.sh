#!/bin/bash

cd rit
make clean
make html
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