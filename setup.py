from setuptools import find_packages, setup

VERSION = '0.1.0'
PACKAGE_NAME = 'text-perturbation'
AUTHOR = 'Dhiraj Poddar'
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email='dhirajpodar@gmail.com',
    install_requires=['nltk','transformers'],
    packages=find_packages()
) 