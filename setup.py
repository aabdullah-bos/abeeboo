import os
import re
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

version = ''
with open('abeeboo/version.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(),
                        re.MULTILINE).group(1)

AUTHOR = 'Aquil H. Abdullah'
EMAIL = 'aquil.abdullah@gmail.com'

extras = {
    'notebooks': ['ipython', 'ipdb', 'jupyter', 'pandas==0.16.2', 'numpy==1.9.2',
                  'matplotlib==1.4.2'],
    'tests': ['nose', 'mock'],
          }
extras['all'] = reduce(lambda x, y: x + y, extras.values())

setup(
    name='abeeboo',
    version=version,
    author=AUTHOR,
    author_email=EMAIL,
    packages=[
        'abeeboo.distance',
        'tests',
             ],
    package_data={'abeeboo.data': ['*.csv', ]},
    url='https://github.com/aabdullah-bos/abeeboo',
    description='Aquilz Utilz',
    long_description=read('README.md'),
    install_requires=[
        'argparse',
    ],
    extras_require=extras,
    test_suite='nose.collector',
    tests_require=['nose', 'mock']
)