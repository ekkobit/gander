# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
autodoc_mock_imports = ["matplotlib"]
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.relpath('../gander/'))
from gander import __version__, __authors__
# import sphinx_bootstrap_theme


# -- Project information -----------------------------------------------------

project = 'Gander'
copyright = '2019, Ekkobit AS'
author = __authors__

# The full version, including alpha/beta/rc tags
release = __version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',

]
# include 'sphinx.ext.imgmath', for math saved as images

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'bootstrap'
#html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_theme = 'alabaster'
html_theme_options = {
    'logo': 'logo.svg',
    'github_user': 'ekkobit',
    'github_repo': 'gander',
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['source/static']


# Todos
todo_include_todos = True

# Math
# imgmath_image_format = 'svg'
