#!/usr/bin/python

from sense_hat import SenseHat
from rpi_ws281x import *
import colorsys
import sys


def hsv2rgb(h, s, v):
    return tuple(int(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

LED_COUNT      = 60      # Number of LED pixels. Change to 120 for both strips
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).     # GPIO pin connected$
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255    # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

strip.begin()

sense = SenseHat()


if (len(sys.argv) == 5):
    h = float(sys.argv[1])
    s = float(sys.argv[2])
    v = float(sys.argv[3])
    p = int(sys.argv[4])
    print(h, s, v, p)

    if (p):
        h = h / 360
        s = s / 100
        v = v / 100
        print(h, s, v)

        print(colorsys.hsv_to_rgb(h, s, v))
        rgb = hsv2rgb(h, s, v)
        print(rgb)
        for i in range(strip.numPixels()):
		    strip.setPixelColor(i, Color(int(rgb[0]*255),int(rgb[1]*255),int(rgb[2]*255)))
		    strip.show()
        sense.clear(rgb)
    else:
        sense.clear(0, 0, 0)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0,0,0))
            strip.show()
