toronado
========

Fast lxml-based CSS stylesheet inliner.

Installation
~~~~~~~~~~~~

This package is hosted on `PyPI <https://pypi.python.org/pypi/toronado>`_ and
can be installed using ``pip`` or ``easy_install``::

    pip install toronado

Usage
~~~~~

.. code::

    >>> from lxml import html
    >>> from toronado import inline
    >>> document = """<html>
    ... <head>
    ...     <style type="text/css">
    ...         h1 { color: red; }
    ...     </style>
    ... </head>
    ... <body><h1>Hello, world.</h1></body>
    ... </html>"""
    >>> tree = html.document_fromstring(document)
    >>> inline(tree)
    >>> print html.tostring(tree)
    <html><head></head><body><h1 style="color: red">Hello, world.</h1></body></html>

Command Line Usage
------------------

To inline a file directly from the command line, you can use the following::

    python -m toronado input.html

The inlined HTML will be printed to your shell's ``stdout`` stream, and can
also be redirected to a file::

    python -m toronado input.html > output.html
