from microbit import * # tell python code will run on micro:bit
display.clear() # makes sure all display LEDs are off
while True:
    display.set_pixel(0,1,9) # column = 0, row = 1, brightness = 9 (max)
    sleep(1000) # sleep time in milliseconds (ms), 1000 ms = 1 s
    display.set_pixel(0,1,0) # column = 0, row = 1, brightness = 0 (off)
    sleep(1000) # sleep time in milliseconds (ms), 1000 ms = 1 s
