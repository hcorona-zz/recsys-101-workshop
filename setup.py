#
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = 0.01
exec(open('src/_version.py').read())
readme = open('README.md').read()
description = 'library for recommender systems interactive workshop'


# For tests
setup_requires = [
    'coverage',
    'flake8',
    'nose',
    'pandas',
    'numpy',
    'matplotlib',
]

setup(
    name='recsys-101-workshop',
    version=__version__,
    description=description,
    long_description=readme,
    packages=['src'],
    package_dir={'recsys-101-workshop': 'src'},
    include_package_data=True,
    setup_requires=setup_requires,
    test_suite='tests',
    authors ='Humberto Corona, ',
)
