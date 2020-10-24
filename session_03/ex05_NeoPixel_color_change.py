from microbit import *          # import Micro:Bit module
from neopixel import NeoPixel   # import NeoPixel module

# Note: the NeoPixels will only light up if your robot has batteries and is turned on

# 4 NeoPixels all connected to pin 15
neo_pixels = NeoPixel(pin15,4)

# define colors as list variables
color_red = [255,0,0] # red
color_grn = [0,255,0] # green
color_blu = [0,0,255] # blue
color_wht = [255,255,255] # white

while True:
    # set all neopixels to red
    neo_pixels[0] = color_red
    neo_pixels[1] = color_red
    neo_pixels[2] = color_red
    neo_pixels[3] = color_red
    neo_pixels.show()
    sleep(1000)
    # set all neopixels to green
    neo_pixels[0] = color_grn
    neo_pixels[1] = color_grn
    neo_pixels[2] = color_grn
    neo_pixels[3] = color_grn
    neo_pixels.show()
    sleep(1000)
    # set all neopixels to blue
    neo_pixels[0] = color_blu
    neo_pixels[1] = color_blu
    neo_pixels[2] = color_blu
    neo_pixels[3] = color_blu
    neo_pixels.show()
    sleep(1000)
    # set pixels to different colors
    neo_pixels[0] = color_red
    neo_pixels[1] = color_grn
    neo_pixels[2] = color_blu
    neo_pixels[3] = color_wht
    neo_pixels.show()
    sleep(1000)