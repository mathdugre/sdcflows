"""
Configuration file for the Sphinx documentation builder.

This file does only contain a selection of the most common options. For a
full list see the documentation:
http://www.sphinx-doc.org/en/master/config

"""
from packaging.version import Version
from sdcflows import __version__, __copyright__, __packagename__

# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.append(os.path.abspath("sphinxext"))

# -- Project information -----------------------------------------------------
project = __packagename__
copyright = __copyright__
author = "The SDCflows Developers"

# The short X.Y version
version = Version(__version__).public
# The full version, including alpha/beta/rc tags
release = __version__

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.githubpages",
    "sphinx.ext.ifconfig",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinxcontrib.apidoc",
    "nipype.sphinxext.apidoc",
    "nipype.sphinxext.plot_workflow",
]

autodoc_mock_imports = [
    "matplotlib",
    "nilearn",
    "nipy",
    "nitime",
    "numpy",
    "pandas",
    "seaborn",
    "skimage",
    "svgutils",
    "transforms3d",
]

# Accept custom section names to be parsed for numpy-style docstrings
# of parameters.
napoleon_use_param = False
napoleon_custom_sections = [
    ("Inputs", "Parameters"),
    ("Outputs", "Parameters"),
    ("Attributes", "Parameters"),
    ("Mandatory Inputs", "Parameters"),
    ("Optional Inputs", "Parameters"),
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

numfig = True

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "api/sdcflows.rst",
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_js_files = [
    "js/version-switch.js",
]
html_css_files = [
    "css/version-switch.css",
]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "sdcflowsdoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "sdcflows.tex",
        "SDCFlows Documentation",
        "The SDCFlows Developers",
        "manual",
    ),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "sdcflows", "SDCFlows Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "sdcflows",
        "SDCFlows Documentation",
        author,
        "SDCFlows",
        "One line description of project.",
        "Miscellaneous",
    ),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]


# -- Extension configuration -------------------------------------------------

apidoc_module_dir = "../sdcflows"
apidoc_output_dir = "api"
apidoc_excluded_paths = ["conftest.py", "*/tests/*", "tests/*", "data/*"]
apidoc_separate_modules = True
apidoc_extra_args = ["--module-first", "-d 1", "-T"]

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "bids": ("https://bids-standard.github.io/pybids/", None),
    "nibabel": ("https://nipy.org/nibabel/", None),
    "nipype": ("https://nipype.readthedocs.io/en/latest/", None),
    "niworkflows": ("https://www.nipreps.org/niworkflows/", None),
    "smriprep": ("https://www.nipreps.org/smriprep/", None),
    "templateflow": ("https://www.templateflow.org/python-client", None),
}

# -- Options for versioning extension ----------------------------------------
scv_show_banner = True
