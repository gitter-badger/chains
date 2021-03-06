import os
import sys

from setuptools import setup

# Project Information 
package_name = 'chains'
description = 'Exploratory Python Chained Generator Project'

author = 'Brian Wylie'
author_email ='brifordwylie@gmail.com'

scripts = []
packages = ['chains', 'chains.links', 'chains.sinks', 'chains.sources', 'chains.utils']

requirements = ['pypcap', 'dpkt']
test_requirements = []

# Pull in the version from the package
package = __import__(package_name)
version = package.__version__

# Pull in the package
package = __import__(package_name)

setup(
      name=package_name,
      version=package.__version__,
      author=package.__author__,
      url=package.__url__,
      description=description,
      packages=packages,
      install_requires=requirements,
      license='MIT',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
      ],
      tests_require=test_requirements
)
