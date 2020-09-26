"""Setup for the tiger_assessment package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Sandeep Kiran Gudla",
    author_email="sandeep.kiran.gudla@gmail.com",
    name='Tiger_Assessment',
    license='NA',
    description='Tiger_Assessment is a python package for developed as a part of interview process.',
    version='v0.0.1',
    long_description=README,
    url='https://github.com/sandeepkirangudla/tiger_assessment',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['pandas',
                      'numpy',
                      'matplotlib',
                      'seaborn',
                      'os',
                      'logging',
                      'datetime',
                      'subprocess',
                      'zipline',
                      'json',
                      'sys'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: NA',
        'License :: OSI Approved :: NA',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6.8',
        'Topic :: Machine Learning :: Libraries',
        'Topic :: Machine Learning Development :: Libraries :: Python Modules',
        'Intended Audience :: Tiger',
    ],
)