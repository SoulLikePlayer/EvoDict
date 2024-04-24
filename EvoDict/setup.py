from setuptools import setup, find_packages

setup(
    name='EvoDict',
    version='1.0',
    packages=find_packages(),
    author='Louis',
    author_email='louislazare.pro@gmail.com',
    description='Une classe représentant un dictionnaire évolué',
    install_requires=[
        'tabulate',
        'networkx',
        'matplotlib'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
)
