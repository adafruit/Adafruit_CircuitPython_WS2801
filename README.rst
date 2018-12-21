Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-ws2801/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/ws2801/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.com/adafruit/Adafruit_CircuitPython_WS2801.svg?branch=master
    :target: https://travis-ci.com/adafruit/Adafruit_CircuitPython_WS2801
    :alt: Build Status

Higher level WS2801 driver that presents the LED string as a sequence.
It is the same api as the
`NeoPixel library <https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel>`_.

Colors are stored as tuples by default. However, you can also use int hex syntax
to set values similar to colors on the web. For example, ``0x800000`` (``#800000``
on the web) is equivalent to ``(0x80, 0, 0)``.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

This example demonstrates the library driving 
`a strand of 25 RGB leds <https://www.adafruit.com/product/322>`_ by a
`Gemma M0 <https://www.adafruit.com/product/3501>`_ using the hardware SPI capable outputs.

.. code-block:: python

    import board
    import adafruit_ws2801

    leds = adafruit_ws2801.WS2801(board.D2, board.D0, 25)
    leds.fill((0x80, 0, 0))

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_WS2801/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

Zip release files
-----------------

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix adafruit-circuitpython-ws2801 --library_location .

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
