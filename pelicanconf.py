#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'redlotus'
SITENAME = 'redlotus'
SITEURL = 'http://redlotus.github.io/nerd'

PATH = 'content'

TIMEZONE = 'Asia/Ho_Chi_Minh'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('pelican', 'http://getpelican.com'),
         ('python.org', 'http://python.org'),
         ('archlinuxvn', 'http://archlinuxvn.org'),)

# Social widget
SOCIAL = (('github', 'https://github.com/redlotus'),
          ('twitter', 'https://twitter.com/r3d10tu5'),)

# DEFAULT_PAGINATION = 3
# URL settings
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# Formatting for dates
DEFAULT_DATE_FORMAT = ('%a %b %d %Y')

# Specify theme
THEME = "/home/redlotus/dev/lotus"
# Plugins
PLUGIN_PATHS = ["/home/redlotus/dev/pelican-plugins"]
PLUGINS = ["neighbors"]

# Menu
MENUITEMS = (('main', 'index.html'),
             ('about', 'pages/about.html'),
             ('resume', 'pages/cv.html'),)
# output
OUTPUT_RETENTION=[".git"]
