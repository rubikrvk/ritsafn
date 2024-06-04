# Set default values for Sphinx options and build command if they are not already set.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build

# Define the source directory and the build directory.
SOURCEDIR     = .
BUILDDIR      = _build

# Target to display help from Sphinx
help:
	# Run the Sphinx build command with the 'help' target
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Declare phony targets that do not correspond to actual files
.PHONY: help Makefile

# Target to build PDF from LaTeX
latexpdf:
	# Run the Sphinx build command with the 'latex' builder
	@$(SPHINXBUILD) -t latex -b latex "$(SOURCEDIR)" "$(BUILDDIR)/latex" $(SPHINXOPTS) $(O)
	# Change directory to the build/latex directory and make the PDF
	@$(MAKE) -C "$(BUILDDIR)/latex" all-pdf

# Generic target pattern for Sphinx build
%: Makefile
	# Run the Sphinx build command with the specified target
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
