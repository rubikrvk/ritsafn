#!/bin/bash

# Búa til HTML skrár með "-b dirhtml" (sem lætur alla hlekki vísa á "<slóð>/", en ekki á "<slóð>/<skrá>.html" eins og "-b html" gerir)
cd rit
make clean
sphinx-build -b dirhtml . _build/html

# Fjarlægja "type" úr favicon.ico og apple-touch-icon.png (sbr. https://dev.to/masakudamatsu/favicon-nightmare-how-to-maintain-sanity-3al7)
find _build/html/ -name '*.html' -exec sed -i '' -e 's#<link rel="icon" href="https://rit.rubik.is/_static/favicon/favicon.ico" sizes="48x48"[^>]*>#<link rel="icon" href="https://rit.rubik.is/_static/favicon/favicon.ico" sizes="48x48">#' {} +
find _build/html/ -name '*.html' -exec sed -i '' -e 's#<link rel="apple-touch-icon" href="https://rit.rubik.is/_static/favicon/apple-touch-icon.png"[^>]*>#<link rel="apple-touch-icon" href="https://rit.rubik.is/_static/favicon/apple-touch-icon.png">#' {} +

# Breyta <title> á forsíðu, með því að fjarlægja "* &ndash; "
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
