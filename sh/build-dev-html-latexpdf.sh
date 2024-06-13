#!/bin/bash

# Búa til HTML skrár með "-b html" (sem lætur alla hlekki vísa á "<slóð>/<skrá>.html", en ekki á "<slóð>/" eins og "-b dirhtml" gerir)
cd rit
make clean
sphinx-build -b html -t dev . _build/html

# Keyra Prettier á allar HTML skrár
find _build/html/ -name "*.html" -exec prettier --config ../json/.prettierrc.json --write {} +

# Bæta við íslenskum þýðingum fyrir sphinx_copybutton
cp -f ../js/copybutton-is.js _build/html/_static/copybutton.js

# Búa til PDF fyrir öll rit, færa í rótarmöppu og eyða út _build/latex/
make latexpdf
mv _build/latex/*.pdf _build/html/
rm -rf _build/latex/

# Skoða allar undirmöppur
for dir in */ ; do

  # Athuga hvort undirmappa byrji ekki á "_" (til að útiloka "_build", "_locale", "_static", "_templates", o.s.frv.)
  if [[ "$dir" != _* ]]; then

    # Athuga hvort tiltekin mappa sé til í rit/_build/html (hún er það ekki, ef mappan er t.d. í exclude_patternsí conf.py)
    if [[ -d "_build/html/${dir%/}/" ]]; then

      # Fara í undirmöppu og búa til PDF skrár
      cd "$dir"
      make clean
      make latexpdf

      # Færa PDF skrár í undirmöppu og eyða út _build/
      mv _build/latex/*.pdf "../_build/html/${dir%/}/"
      rm -rf _build/
      cd ..

    fi
  fi
done
