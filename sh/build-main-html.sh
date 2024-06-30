#!/bin/bash

# Búa til HTML skrár með "-b html" (sem lætur alla hlekki vísa á "<slóð>/<skrá>.html", en ekki á "<slóð>/" eins og "-b dirhtml" gerir)
cd rit
make clean
sphinx-build -b html . _build/html

# Fjarlægja "type" úr favicon.ico og apple-touch-icon.png (sbr. https://dev.to/masakudamatsu/favicon-nightmare-how-to-maintain-sanity-3al7)
find _build/html/ -name '*.html' -exec sed -i '' -e 's#<link rel="icon" href="https://rit.rubik.is/_static/favicon/favicon.ico" sizes="48x48"[^>]*>#<link rel="icon" href="https://rit.rubik.is/_static/favicon/favicon.ico" sizes="48x48">#' {} +
find _build/html/ -name '*.html' -exec sed -i '' -e 's#<link rel="apple-touch-icon" href="https://rit.rubik.is/_static/favicon/apple-touch-icon.png"[^>]*>#<link rel="apple-touch-icon" href="https://rit.rubik.is/_static/favicon/apple-touch-icon.png">#' {} +

# Breyta <title> á forsíðu, með því að fjarlægja "* &ndash; "
sed -i '' -e 's#<title>.* &ndash; Ritsafn RÚBIK Reykjavíkur</title>#<title>Ritsafn RÚBIK Reykjavíkur</title>#' _build/html/index.html

# Keyra Prettier á allar HTML skrár
find _build/html/ -name "*.html" -exec prettier --config ../json/.prettierrc.json --write {} +

# Bæta við íslenskum þýðingum fyrir sphinx_copybutton
cp -f ../js/copybutton-is.js _build/html/_static/copybutton.js