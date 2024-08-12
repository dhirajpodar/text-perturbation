from setuptools import find_packages, setup

VERSION = '0.1.0'
PACKAGE_NAME = 'text-perturbation'
REPO_NAME = "text-perturbation"
AUTHOR = 'Dhiraj Poddar'
AUTHOR_USER_NAME = 'dhirajpodar'
REPO_NAME = 'text-perturbation'
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email='dhirajpodar@gmail.com',
    install_requires=['nltk','transformers'],
    packages=find_packages(where="src"),
    url=f"https://githhub.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://githhub.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"}
) 