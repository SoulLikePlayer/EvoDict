from setuptools import setup, find_packages

setup(
    name='EvoDict',
    version='0.1',
    packages=find_packages(),
    author='Louis',
    author_email='louislazare.pro@gmail.com',
    description='Une classe représentant un dictionnaire évolué',
    install_requires=[
        'tabulate',
        'networkx',
        'matplotlib',
        'string'
        'tkinter',
        'random'
    ],
)
