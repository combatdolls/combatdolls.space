set windows-powershell := true

# SPHINXOPTS := "-a -E -v"
SPHINXOPTS := "-j auto"
SOURCEDIR  := "source"
BUILDDIR   := "build"


# Show this help
@help:
  just --list


# Show sphinx help
@sphinx-help:
  just build help


# Set up dev environments
install:
  pipenv install --dev


# Run sphinx autobuild against the docs.
serve:
  pipenv run sphinx-autobuild --port 0 --open-browser "{{SOURCEDIR}}" "{{BUILDDIR}}/html"


# Do a sphinx build
build KIND="html":
  pipenv run sphinx-build -M {{KIND}} "{{SOURCEDIR}}" "{{BUILDDIR}}" {{SPHINXOPTS}}


# Run sphinx linkcheck
@linkcheck:
  just build linkcheck


# Clean up built files
@clean:
  just build clean
