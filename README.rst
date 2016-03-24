Bayesian Online Changepoint Detection
================================================================================

**Author**: Asher Bender

**Date**: March 2016

**License**: `None <http://choosealicense.com/no-license/>`_


Overview
--------------------------------------------------------------------------------

**Note: This algorithm is currently under construction and will be open-sourced
when it is in a functional state.**

This code implements `Bayesian online changepoint detection
<http://arxiv.org/abs/0710.3742>`_ using the `Bayesian linear model
<http://en.wikipedia.org/wiki/Bayesian_linear_regression>`_ `[1, 2, 3, 4]
<https://github.com/asherbender/bayesian-online-changepoint-detection#references>`_.
In this algorithm, changepoints are considered as "*abrupt variations in the
generative parameters of a data sequence*" [1].

The code provided in this repository is a Python port of the original `MATLAB
<http://hips.seas.harvard.edu/content/bayesian-online-changepoint-detection>`_
code with the *significant* advantage that it can perform updates to linear
models with multiple coefficients.

Installation
--------------------------------------------------------------------------------

This code supports installation using pip (via `setuptools
<https://pypi.python.org/pypi/setuptools>`_). To install from the git
repository:

.. code-block:: bash

    git clone https://github.com/asherbender/bayesian-online-changepoint-detection
    cd bayesian-online-changepoint-detection
    sudo pip install .

To uninstall the package:

.. code-block:: bash

    pip uninstall bocd


References
--------------------------------------------------------------------------------

The Bayesian online changepoint detection algorithm was implemented using the
following reference:

.. _[1]: http://arxiv.org/abs/0710.3742

`[1]`_ Adams, R. P. and MacKay, D. J.C., Bayesian online changepoint
       detection, University of Cambridge, 2007

The Bayesian linear model module was created using the following references:

.. _[2]: http://www.cs.ubc.ca/~murphyk/MLbook/
.. _[3]: http://research.microsoft.com/en-us/um/people/cmbishop/prml/
.. _[4]: http://www.cs.ubc.ca/~murphyk/Papers/bayesGauss.pdf

`[2]`_ Murphy, K. P., Machine learning: A probabilistic perspective,
       The MIT Press, 2012

`[3]`_ Bishop, C. M, Pattern Recognition and Machine Learning (Information
       Science and Statistics), Jordan, M.; Kleinberg, J. & Scholkopf, B.
       (Eds.), Springer, 2006

`[4]`_ Murphy, K. P., Conjugate Bayesian analysis of the Gaussian distribution,
       Department of Computer Science, The University of British Columbia, 2007

See also
--------------------------------------------------------------------------------

An implementation of the Bayesian linear model can be found in the following
`repository <https://github.com/asherbender/bayesian-linear-model>`_.
