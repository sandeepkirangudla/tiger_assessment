"""Setup for the tiger_assessment package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Sandeep Kiran Gudla",
    author_email="gsandeepkiran@gmail.com",
    name='Tiger_Assessment',
    license='NA',
    description='Tiger_Assessment is a python package for developed as a part of interview process.',
    version='v0.0.17',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/sandeepkirangudla/tiger_assessment',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['pandas',
                      'numpy'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)