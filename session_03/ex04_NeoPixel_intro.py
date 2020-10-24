from microbit import *          # import Micro:Bit module
from neopixel import NeoPixel   # import NeoPixel module

# Note: the NeoPixels will only light up if your robot has batteries and is turned on

# 4 NeoPixels all connected to pin 15
neo_pixels = NeoPixel(pin15,4)

# set NeoPixels to different colors using RGB color codes
neo_pixels[0] = [255,0,0] # red
neo_pixels[1] = [0,255,0] # green
neo_pixels[2] = [0,0,255] # blue
neo_pixels[3] = [255,255,255] # white
neo_pixels.show() # write the color code values to the NeoPixels
