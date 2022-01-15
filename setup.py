#!/usr/bin/env python
import os
import glob
from setuptools import setup
from idlexlib._version import __version__

def get_dir(d):
    return glob.glob('%s/*' % d)


ldesc = """IdleX is a collection of over 20 extensions for the Python IDLE environment."""

setup(name='idlex',
      version=__version__,
      description='IDLE Extensions for Python',
      author='Roger D. Serwy',
      author_email='roger.serwy@gmail.com',
      url='http://idlex.sourceforge.net',
      packages=['idlexlib',
                'idlexlib.extensions',
                'idlexlib.idlefork.idlelib'],
      package_dir = {'idlexlib': 'idlexlib',
                     'idlexlib.idlefork.idlelib': 'idlexlib/idlefork/idlelib'},
      package_data = {'idlexlib.idlefork.idlelib':['Icons/*']},
      include_package_data=True,
      scripts = get_dir('scripts'),
      license='NCSA License',
      long_description=ldesc,
      classifiers = [
          'Development Status :: 5 - Production/Stable',
          'Framework :: IDLE',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: University of Illinois/NCSA Open Source License',
          'License :: OSI Approved :: Python Software Foundation License',
          'Topic :: Text Editors :: Integrated Development Environments (IDE)',
          'Operating System :: OS Independent',
        ],
     )
