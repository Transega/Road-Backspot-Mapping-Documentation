# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import date
# sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
today = date.today()

year = today.year




# -- Project information -----------------------------------------------------

project = 'Road Blackspot Mapping Admin Manual'
copyright = str(year)+', St. Johns Ambulance'
author = 'St. Johns Ambulance'

# The full version, including alpha/beta/rc tags
release = 'V01'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

html_last_updated_fmt = '%b %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

html_context = {
    # "display_github": True,  # Add 'Edit on Github' link instead of 'View page source'
    "last_updated": str(today),
    "commit": False,
}

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/custom.css', 
]

# Build PDF & ePub
formats = ['pdf', 'epub']