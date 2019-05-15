#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import tempfile


SITENAME = os.environ['PELICAN_SITENAME']
AUTHOR = os.environ['PELICAN_AUTHOR']
SITEURL = os.environ['PELICAN_SITEURL']
PATH = os.path.expanduser(os.environ['PELICAN_CONTENT'])
ARTICLE_EXCLUDES = PAGE_EXCLUDES = os.environ.get('PELICAN_EXCLUDES', '').split(':')
OUTPUT_PATH = os.path.expanduser(os.environ['PELICAN_OUTPUT_PATH'])
PLUGIN_PATHS = [
    os.path.expanduser(plugin_path)
    for plugin_path in os.environ['PELICAN_PLUGIN_PATHS'].split(':')
]

THEME = os.path.expanduser(os.environ.get('PELICAN_THEME', 'notmyidea'))


DEFAULT_LANG = 'en'
TIMEZONE = 'Europe/London'

DEFAULT_PAGINATION = 30

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/index.html'
CATEGORY_URL = '{slug}/'
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

DEFAULT_DATE = 'fs'
FILENAME_METADATA = r'(?P<title>(?P<date>\d{4}\.\d{2}\.\d{2})?.*)'

try:
    cache_tag = os.environ['PELICAN_PEPYS_CACHE_TAG']
    caches_path = os.environ.get(
        'PELICAN_PEPYS_CACHES_PATH',
        os.path.join(tempfile.gettempdir(), 'pelipepys_caches')
    )
    CACHE_PATH = os.path.join(caches_path, cache_tag)
    CACHE_CONTENT = True
    LOAD_CONTENT_CACHE = True
    CHECK_MODIFIED_METHOD = 'mtime'
    # CONTENT_CACHING_LAYER = 'generator'
    # WITH_FUTURE_DATES = False
except KeyError:
    # Caching disabled
    DELETE_OUTPUT_DIRECTORY = True

# No feeds for diaries
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGINS = [
    'neighbors',
    'section_number',
    'pelican-toc',
    'tipue_search',
]
if os.environ.get('PELICAN_PEPYS_MINIFY_CSS', 'no').lower() in ('true', 'yes'):
    PLUGINS.append('assets')

DIRECT_TEMPLATES = [
    'index',
    'tags',
    'categories',
    'authors',
    'archives',
    'search',
]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.admonition': {},
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.smarty': {},
        'mdx_truly_sane_lists': {},
        'pymdownx.magiclink': {},
    },
    'output_format': 'html5',
}

TOC = {
    'TOC_HEADERS': '^h[1-6]',
    'TOC_RUN': 'true',
    'TOC_INCLUDE_TITLE': 'false',
}
