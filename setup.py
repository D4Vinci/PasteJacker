#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

with open(os.path.join('PasteJacker', 'Core', 'Data', 'version.txt')) as f:
    version = f.read().strip()

with open('README.md') as f:
    des = f.read().strip()

setup(name='PasteJacker',
    version=version,
    author = "Karim Shoair (D4Vinci)",
    description='Hacking systems with the automation of PasteJacking attacks.',
    long_description=des,
    url='https://github.com/D4Vinci/PasteJacker',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    install_requires=[
        'Jinja2',
        'readline;platform_system!="Windows"',
        'gnureadline;platform_system!="Windows"'
    ],
    entry_points={
        'console_scripts': [
            'pastejacker = PasteJacker.main:menu',
        ],
    },
)
