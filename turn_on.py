#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, sys, inspect, ast
import RPi.GPIO as GPIO

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

# Configure the count of pixels:
PIXEL_COUNT = 32

# other settings
SPI_PORT = 0
SPI_DEVICE = 0

pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)


################################################################################
# DEFINE YOUR FUNCTIONS HERE
################################################################################

def set_rgb_color(pxels, r=255, g=255, b=255):
    # cast from string to int
    r, g, b = int(float(r)), int(float(g)), int(float(b))
    pxels.set_pixels(Adafruit_WS2801.RGB_to_color(r, g, b))
    pxels.show()


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(1)

    cmdargs = sys.argv[1:]
    set_rgb_color(pixels, cmdargs[0], cmdargs[1], cmdargs[2])
