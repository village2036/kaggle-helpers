#!/usr/bin/env python

from distutils.core import setup

setup(name='kaggle-utilities',
      version='1.0',
      description='Helper utilities for kaggle notebooks',
      author='village2036',
      author_email='dev@village2036.com',
      url='https://github.com/village2036/kaggle-utilities',
      packages=['village2036'],
      requires=['numpy','pandas', 'geopandas','matplotlib','kaggle']
     )
