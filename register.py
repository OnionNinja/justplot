#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pypandoc
import os


doc = pypandoc.convert('README.md','rst')
with open('README.rst','w+', encoding='utf-8') as f:
    f.write(doc)
os.system('./setup.py sdist upload')
os.remove('README.rst')
