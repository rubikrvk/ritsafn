#!/bin/bash

# Búa til HTML skrár með "-b html -t dev" (sem lætur alla hlekki vísa á "<slóð>/<skrá>.html", en ekki á "<slóð>/" eins og "-b dirhtml" gerir)
cd rit
make clean
sphinx-build -b html -t dev . _build/html

# Bæta "noindex, nofollow" við <head> í öllum HTML skrám fyrir DEV
find _build/html/ -name '*.html' -exec sed -i '' -e 's/<head>/<head>\n<meta name="robots" content="noindex, nofollow">/' {} +

# Breyta slóð á favicon í https://rit-dev.rubik.is/ fyrir DEV
find _build/html/ -name '*.html' -exec sed -i '' -e 's|href="https://rit.rubik.is/|href="https://rit-dev.rubik.is/|g' {} +

# Fjarlægja Google Tag Manager kóða fyrir DEV
find _build/html/ -name '*.html' -exec sed -i '' -e '/<script>(function(w,d,s,l,i){w\[l\]=w\[l\]\|\|\[\];w\[l\]\.push(/,/GTM-PL8JH23F/ d' {} \;
find _build/html/ -name '*.html' -exec sed -i '' -e '/  <noscript><iframe src="https:\/\/www.googletagmanager.com\/ns.html?id=GTM-PL8JH23F"/,/<\/noscript>/d' {} \;

# Breyta <title> á forsíðu, með því að fjarlægja "* &ndash; " (sem er skilgreint í "_templates/layout.html")
sed -i '' -e 's#<title>.* &ndash; Ritsafn RÚBIK Reykjavíkur</title>#<title>Ritsafn RÚBIK Reykjavíkur</title>#' _build/html/index.html

# Keyra Prettier á allar HTML skrár
find _build/html/ -name "*.html" -exec prettier --config ../json/.prettierrc.json --write {} +

# Bæta við íslenskum þýðingum fyrir sphinx_copybutton
cp -f ../js/copybutton-is.js _build/html/_static/copybutton.js