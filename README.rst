ijroi |Build Status| |Coverage Status| |PyPI page| |MIT license|
================================================================

Reads `ImageJ <http://imagej.net/Welcome>`__ ROIs into numpy arrays. Use
it like:

.. code:: python

    >>> import ijroi
    >>> with open("my_roi.roi", "rb") as f:
    ...     roi = ijroi.read_roi(f)
    ...
    >>> isinstance(roi, np.ndarray)
    True

read\_roi returns a Nx2 array, where each row is a (row, column) or (y,
x) pair.

Based on `Luis Pedro Coelho <https://github.com/luispedro>`__'s
`readroi.py gist <https://gist.github.com/luispedro/3437255>`__.

License
=======

ijroi is offered under the MIT license.

Contributors
============

ijroi is maintained by Tim D. Smith. The core functionality was
implemented by Luis Pedro Coelho.

.. |Build Status| image:: https://travis-ci.org/tdsmith/ijroi.svg?branch=master
   :target: https://travis-ci.org/tdsmith/ijroi
.. |Coverage Status| image:: https://coveralls.io/repos/tdsmith/ijroi/badge.svg?branch=master
   :target: https://coveralls.io/r/tdsmith/ijroi?branch=master
.. |PyPI page| image:: https://img.shields.io/pypi/dm/ijroi.svg
   :target: https://pypi.python.org/pypi/ijroi
.. |MIT license| image:: https://img.shields.io/pypi/l/ijroi.svg
   :target: https://github.com/tdsmith/ijroi/blob/master/COPYING
