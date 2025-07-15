# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Combat Dolls Clan'
copyright = '2025, Combat Dolls Destiny Clan'
author = 'Waterfall of Lead, Bee Stings from Shadows'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_last_updated_by_git',
    'sphinxext.opengraph',
]

templates_path = ['_templates']
exclude_patterns = []

# html_additional_pages = {
#     "index": "warp-page.html"
# }

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_title = 'Combat Dolls'

# html_logo = '_static/pink-circles.png'

html_js_files = [
    'three.min.js',
]

html_theme_options = {
    "light_css_variables": {
        "font-stack": "'Josefin Sans', sans-serif",
    },
}

ogp_site_url = 'https://combatdolls.space/'
ogp_use_first_image = True
