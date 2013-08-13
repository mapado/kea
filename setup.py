import re

from os.path import join, dirname
from setuptools import setup

VERSION = re.search(
    "__version__ = '([^']+)'", open(
        join(dirname(__file__), 'kea', '__init__.py')
        ).read().strip()).group(1)

setup(
    name='kea',
    version='0.2.2',
    description='A tokenizer for French',
    author='Florian Boudin',
    author_email='florian.boudin@univ-nantes.fr',
    maintainer='Balthazar Rouberol',
    maintainer_email='balthazar@mapado.com',
    license='Creative Commons',
    long_description=open('README.md').read(),
    packages=['kea'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Text Processing :: Linguistic',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
        ]
)
