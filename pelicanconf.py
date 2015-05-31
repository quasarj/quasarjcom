#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

LOAD_CONTENT_CACHE = False

AUTHOR = 'Quasar Jarosz'
SITENAME = 'Quasarj.com'
# SITESUBTITLE = 'Where I talk about some things'
SITEURL = 'http://quasarj.com'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

# THEME = 'simple'
# THEME = 'notmyidea'
# THEME = 'themes/quasar'
# THEME = 'themes/blueidea'

# -- themes ordered by current preference

# I like this one A LOT
# Very nice script font for titles.
# The title needs to be kept shor to fit, and I would need to edit
# the css to adjust the color of code blocks.
THEME = 'themes/subtle'

# very nice blocky minimal clutter
# THEME = 'themes/chunk'

# very nice, minimal but stylish. Syntax highlighting is good, but
# bullets need fixing. Very grey.
# THEME = 'themes/pelican-mockingbird'

# quite good as well, simple and functional
# The side bar is a bit weird looking, and it cuts off code blocks
# without good indication that you need to click to get to the full post
# THEME = 'themes/svbtle'

# big, but nice
# THEME = 'themes/fresh'

# CSS_FILE = 'wide.css'

GITHUB_URL = 'http://github.com/quasarj/quasarjcom'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
LINKS = ()

# Social widget
SOCIAL = ()
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
