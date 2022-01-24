Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-ws2801/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/ws2801/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_WS2801/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_WS2801/actions/
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

Installing from PyPI
====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-ws2801/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-ws2801

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-ws2801

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-ws2801

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

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/ws2801/en/latest/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_WS2801/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
