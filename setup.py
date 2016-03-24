from setuptools import setup

description = 'Implementation of the Bayesian online changepoint detection '
description += 'algorithm.'

setup(
    name='bocd',
    version='1.0',
    author='Asher Bender',
    author_email='a.bender.dev@gmail.com',
    description=(description),
    py_modules=['bocd'],
    install_requires=[
        'numpy',
        'scipy',
        'Sphinx',
    ]
)
