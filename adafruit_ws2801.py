# SPDX-FileCopyrightText: 2016 Damien P. George (original Neopixel object)
# SPDX-FileCopyrightText: 2017 Ladyada for Adafruit Industries
# SPDX-FileCopyrightText: 2017 Scott Shawcroft for Adafruit Industries
# SPDX-FileCopyrightText: 2018 Kevin J. Walters
# SPDX-FileCopyrightText: 2024 Tim Cocks for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_ws2801` - WS2801 LED pixel string driver
====================================================

* Author(s): Damien P. George, Limor Fried & Scott Shawcroft, Kevin J Walters, Tim Cocks
"""

import adafruit_pixelbuf
import busio
import digitalio

try:
    from typing import Type, Optional
    from circuitpython_typing import ReadableBuffer
    from types import TracebackType
    from microcontroller import Pin
except ImportError:
    pass

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_WS2801.git"

# based on https://github.com/adafruit/Adafruit_CircuitPython_DotStar

START_HEADER_SIZE = 4

# Pixel color order constants
RBG = "PRBG"
"""Red Blue Green"""
RGB = "PRGB"
"""Red Green Blue"""
GRB = "PGRB"
"""Green Red Blue"""
GBR = "PGBR"
"""Green Blue Red"""
BRG = "PBRG"
"""Blue Red Green"""
BGR = "PBGR"
"""Blue Green Red"""


class WS2801(adafruit_pixelbuf.PixelBuf):
    """
    A sequence of WS2801 controlled LEDs.

    :param ~microcontroller.Pin clock: The pin to output dotstar clock on.
    :param ~microcontroller.Pin data: The pin to output dotstar data on.
    :param int n: The number of LEDs in the chain.
    :param float brightness: The brightness between 0.0 and (default) 1.0.
    :param bool auto_write: True if the dotstars should immediately change when
        set. If False, `show` must be called explicitly.
    :param str pixel_order: Set the pixel order on the strip - different
         strips implement this differently. If you send red, and it looks blue
         or green on the strip, modify this! It should be one of the values above.

    Example for Gemma M0:

    .. code-block:: python

        import adafruit_ws2801
        import time
        import board

        darkred = 0x100000

        with adafruit_ws2801.WS2801(board.D2, board.D0, 25, brightness=1.0) as pixels:
            pixels[0] = darkred
            time.sleep(2)
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        clock: Pin,
        data: Pin,
        n: int,
        *,
        brightness: float = 1.0,
        auto_write: bool = True,
        pixel_order: str = "RGB",
    ) -> None:
        self._spi = None
        try:
            self._spi = busio.SPI(clock, MOSI=data)
            while not self._spi.try_lock():
                pass
            self._spi.configure(baudrate=1000 * 1000)
        except ValueError:
            self.dpin = digitalio.DigitalInOut(data)
            self.cpin = digitalio.DigitalInOut(clock)
            self.dpin.direction = digitalio.Direction.OUTPUT
            self.cpin.direction = digitalio.Direction.OUTPUT
            self.cpin.value = False

        # Supply one extra clock cycle for each two pixels in the strip.
        trailer_size = n // 16
        if n % 16 != 0:
            trailer_size += 1

        # Empty header.
        header = bytearray(0)
        # Zero bits, not ones, for the trailer, to avoid lighting up
        # downstream pixels, if there are more physical pixels than
        # the length of this object.
        trailer = bytearray(trailer_size)

        super().__init__(
            n,
            byteorder=pixel_order,
            brightness=brightness,
            auto_write=auto_write,
            header=header,
            trailer=trailer,
        )

    def deinit(self) -> None:
        """Blank out the DotStars and release the resources."""
        self.fill(0)
        self.show()
        if self._spi:
            self._spi.deinit()
        else:
            self.dpin.deinit()
            self.cpin.deinit()

    def __enter__(self) -> "WS2801":
        return self

    def __exit__(
        self,
        exception_type: Optional[Type[type]],
        exception_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        self.deinit()

    def __repr__(self):
        return "[" + ", ".join([str(x) for x in self]) + "]"

    def _ds_writebytes(self, buf: bytearray) -> None:
        for b in buf:
            for _ in range(8):
                self.dpin.value = b & 0x80
                self.cpin.value = True
                self.cpin.value = False
                b = b << 1

    def _transmit(self, buffer: ReadableBuffer) -> None:
        if self._spi:
            self._spi.write(buffer)
        else:
            self._ds_writebytes(buffer)
