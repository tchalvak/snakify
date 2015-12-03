try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Roguelike using libtcod',
    'author': 'Roy R.',
    'url': 'https://github.com/tchalvak',
    'download_url': 'https://github.com/tchalvak',
    'author_email': 'tchalvak.SPam@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['cobra'],
    'scripts': [],
    'name': 'snakify'
}

setup(**config)
