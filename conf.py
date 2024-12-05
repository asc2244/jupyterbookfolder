# conf.py for Sphinx documentation

import os
import sys
from datetime import datetime

# Add the path to the docs source directory
sys.path.insert(0, os.path.abspath('.'))

# General configuration
project = 'My Project'
author = 'Alexa'
release = '1.0.0'
language = 'en'

# Sphinx extensions (add any needed extensions here)
extensions = []

# Paths that contain templates, relative to this directory
templates_path = ['_templates']

# The master toctree document.
master_doc = 'index'

# Options for HTML output
html_theme = 'alabaster'
html_static_path = ['_static']

# Internationalization (if needed)
# language = None  # Set to your language, e.g., 'en' or 'es'

# Additional configurations...
