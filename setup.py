# -*- coding: utf-8 -*-
# **************************************************************************
# *
# * Authors:     Alberto García Mena (alberto.garcia@cnb.csic.es)
# *
# * Unidad de  Bioinformatica of Centro Nacional de Biotecnologia , CSIC
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307  USA
# *
# *  All comments concerning this program package may be sent to the
# *  e-mail address 'scipion@cnb.csic.es'
# *
# **************************************************************************"""A setuptools based setup module.
"""
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
from xmippBase import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='scipion-em-xmippBase',  # Required
    version=__version__,  # Required
    description='Scipion pseudoplugin to deal with the shared xmipp protocols.',  # Required

    long_description=long_description,  # Optional
    url='https://github.com/I2PC/scipion-em-xmippBase',  # Optional
    author='I2PC',  # Optional
    author_email='scipion@cnb.csic.es',  # Optional
    keywords='scipion cryoem imageprocessing Xmipp scipion-3.0',  # Optional
    packages=find_packages(),
    install_requires=[requirements],
    entry_points={  # Optional
    },
    package_data={  # Optional
    }
)


