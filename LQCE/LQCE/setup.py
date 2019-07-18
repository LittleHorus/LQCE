try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'LQCE',
    'author': 'Aximand',
    'url': '',
    'download_url': 'none',
    'author_email': 'dimonchikgvd@gmail.com',
    'version': '0.1_alfa',
    'install_requires': ['nose'],
    'packages': ['LQCE'],
    'scripts': [],
    'name': 'LQCE'
}

setup(**config)