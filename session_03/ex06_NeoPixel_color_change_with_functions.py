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

def neoPixelsColor(RGB):
    # commands all NeoPixels to emit the same specified color 
    # ----- input ------
    # RGB : [intensity_red,intensity_green,intensity_blue] 
    #    where intensity = 0 for off, intensity = 255 for max
    neo_pixels[0] = RGB
    neo_pixels[1] = RGB
    neo_pixels[2] = RGB
    neo_pixels[3] = RGB
    neo_pixels.show()
    
def neoPixelsOff():
    # turns off all NeoPixels 
    neo_pixels.clear()
   
  
while True:
    # set all neopixels to red
    neoPixelsColor(color_red)
    sleep(1000)
    # set all neopixels to green
    neoPixelsColor(color_grn)
    sleep(1000)
    # set all neopixels to blue
    neoPixelsColor(color_blu)
    sleep(1000)
    # set pixels to different colors
    neo_pixels[0] = color_red
    neo_pixels[1] = color_grn
    neo_pixels[2] = color_blu
    neo_pixels[3] = color_wht
    neo_pixels.show()
    sleep(1000)
    # turn off all LEDs
    neoPixelsOff()
    sleep(1000)
