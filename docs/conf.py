# -*- coding: utf-8 -*-
import sys
from contextlib import suppress
from sphinx_celery import conf

sys.path.append('.')

extensions = []

globals().update(conf.build_config(
    'fastasync', __file__,
    project='FastAsync',
    # version_dev='2.0',
    # version_stable='1.4',
    canonical_url='http://fastasync.readthedocs.io',
    webdomain='',
    github_project='99cloud/fastasync',
    copyright='2021-2022',
    html_logo='images/logo.png',
    html_favicon='images/favicon.ico',
    html_prepend_sidebars=[],
    include_intersphinx={'python', 'sphinx'},
    extra_extensions=[
        'sphinx.ext.napoleon',
        'sphinx_autodoc_annotation',
        'alabaster',
    ],
    extra_intersphinx_mapping={
    },
    # django_settings='testproj.settings',
    # from pathlib import Path
    # path_additions=[Path.cwd().parent / 'testproj']
    apicheck_ignore_modules=[
        'fastasync.loop.eventlet',
        'fastasync.loop.gevent',
        'fastasync.loop.uvloop',
        'fastasync.loop._gevent_loop',
        'fastasync.utils',
        'fastasync.utils._py37_contextlib',
        'fastasync.utils.graphs.formatter',
        'fastasync.utils.graphs.graph',
        'fastasync.utils.types',
    ],
))

html_theme = 'alabaster'
html_sidebars = {}
templates_path = ['_templates']

autodoc_member_order = 'bysource'

pygments_style = 'sphinx'

# This option is deprecated and raises an error.
with suppress(NameError):
    del(html_use_smartypants)  # noqa

extensions.remove('sphinx.ext.viewcode')
