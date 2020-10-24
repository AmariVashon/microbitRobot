from microbit import *        # import Micro:Bit module
from neopixel import NeoPixel # import NeoPixel module

# Note: the NeoPixels will only light up if your robot has batteries and is turned on

# 4 NeoPixels all connected to pin 15
neo_pixels = NeoPixel(pin15,4)

# pause between color change
sleep_time = 5 # milliseconds

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
    

while True:
    # fade from red to green
    for count in range(256):
        red = 255 - count
        grn = count
        blu = 0
        neoPixelsColor([red,grn,blu])
        sleep(sleep_time)
    # fade from green to blue
    for count in range(256):
        red = 0
        grn = 255 - count
        blu = count
        neoPixelsColor([red,grn,blu])
        sleep(sleep_time)
    # fade from blue to red
    for count in range(256):
        red = count
        grn = 0
        blu = 255 - count
        neoPixelsColor([red,grn,blu])
        sleep(sleep_time)