project = 'FastAPI Webinar'
html_title = 'FastAPI Webinar'
copyright = '2021, pauleveritt@me.com'
author = 'pauleveritt@me.com'

extensions = [
    'furo',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'furo'
html_static_path = ['_static']
myst_enable_extensions = [
    'colon_fence',
]