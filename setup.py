from setuptools import setup
from version import VERSION
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup \
(   name = 'toothris'
,   version = VERSION
,   description = 'Smooth Tetris clone with a few surprises.'
,   long_description = long_description
,   url = 'http://www.toothris.org'
,   author = 'Toothris Team'
,   author_email = 'team@toothris.org'
,   license = 'GPL'
,   classifiers =
    [   'Development Status :: 5 - Production/Stable'
    ,   'Intended Audience :: End Users/Desktop'
    ,   'Topic :: Games/Entertainment :: Arcade'
    ,   'License :: OSI Approved :: GNU General Public License (GPL)'
    ,   'Programming Language :: Python :: 2.7'
    ,   'Programming Language :: Python :: 2 :: Only'
    ,   'Programming Language :: Python :: Implementation :: Stackless'
    ]
,   keywords = 'tetris game opengl smooth'
)
