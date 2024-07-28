#!/bin/bash

# Búa til HTML skrár með "-b dirhtml" (sem lætur alla hlekki vísa á "<slóð>/", en ekki á "<slóð>/<skrá>.html" eins og "-b html" gerir)
cd rit
make clean
sphinx-build -b dirhtml . _build/html

# Hafa bara eitt <meta name="viewport"...> tag í öllum HTML skrám 
find _build/html/ -name '*.html' -exec sed -i '' '/<meta name="viewport" .*/d' {} +
find _build/html/ -name '*.html' -exec sed -i '' -e 's|<meta charset="utf-8" />|<meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1" />|' {} +

# Breyta <title> á forsíðu, með því að fjarlægja "* &ndash; " (sem er skilgreint í "_templates/layout.html")
sed -i '' -e 's#<title>.* &ndash; Ritsafn RÚBIK Reykjavíkur</title>#<title>Ritsafn RÚBIK Reykjavíkur</title>#' _build/html/index.html

# Keyra Prettier á allar HTML skrár
find _build/html/ -name "*.html" -exec prettier --config ../json/.prettierrc.json --write {} +

# Bæta við íslenskum þýðingum fyrir sphinx_copybutton
cp -f ../js/copybutton-is.js _build/html/_static/copybutton.js

# Búa til PDF skrá fyrir "rit/", færa í "_build/html/" og eyða út "_build/latex/"
make latexpdf
mv _build/latex/*.pdf _build/html/
rm -rf _build/latex/

# Skoða allar undirmöppur
for dir in */ ; do

  # Athuga hvort undirmappa byrji ekki á "_" (til að útiloka "_build", "_locale", "_static", "_templates", o.s.frv.)
  if [[ "$dir" != _* ]]; then

    # Athuga hvort tiltekin mappa sé til í "rit/_build/html/" (hún á ekki að vera til ef mappan er tilgreind í exclude_patterns í conf.py)
    if [[ -d "_build/html/${dir%/}/" ]]; then

      # Fara í undirmöppu og búa til PDF skrár
      cd "$dir"
      make clean
      make latexpdf

      # Færa PDF skrár í undirmöppu og eyða út "_build/"
      mv _build/latex/*.pdf "../_build/html/${dir%/}/"
      rm -rf _build/
      cd ..

    fi
  fi
done
