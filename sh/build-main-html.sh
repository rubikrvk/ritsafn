#!/bin/bash

# Búa til HTML skrár með "-b html" (sem lætur alla hlekki vísa á "<slóð>/<skrá>.html", en ekki á "<slóð>/" eins og "-b dirhtml" gerir)
cd rit
make clean
sphinx-build -b html . _build/html

# Hafa bara eitt <meta name="viewport"...> tag í öllum HTML skrám 
find _build/html/ -name '*.html' -exec sed -i '' '/<meta name="viewport"/d' {} +
find _build/html/ -name '*.html' -exec sed -i '' -e 's|<meta charset="utf-8" />|<meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1" />|' {} +

# Breyta <title> á forsíðu, með því að fjarlægja "* &ndash; " (sem er skilgreint í "_templates/layout.html")
sed -i '' -e 's#<title>.* &ndash; Ritsafn RÚBIK Reykjavíkur</title>#<title>Ritsafn RÚBIK Reykjavíkur</title>#' _build/html/index.html

# Keyra Prettier á allar HTML skrár
find _build/html/ -name "*.html" -exec prettier --config ../json/.prettierrc.json --write {} +

# Bæta við íslenskum þýðingum fyrir sphinx_copybutton
cp -f ../js/copybutton-is.js _build/html/_static/copybutton.js