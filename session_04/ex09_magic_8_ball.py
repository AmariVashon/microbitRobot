from microbit import *
from random import *

image8 = Image( "00900:"
                "09090:"
                "00900:"
                "09090:"
                "00900:")

while True:
    display.show(image8)
    if accelerometer.was_gesture("shake"):
        value = randint(1,6)
        if value == 1:
            display.scroll("yes")
        elif value == 2:
            display.scroll("no")
        elif value == 3:
            display.scroll("maybe")
        elif value == 4:
            display.scroll("try again")
        elif value == 5:
            display.scroll("ask again later")
        else:
            display.scroll("don't count on it")