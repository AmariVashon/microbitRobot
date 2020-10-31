from microbit import *
from random import *
while True:
    if accelerometer.was_gesture("shake"):
        display.scroll(randint(1,6))
        sleep(1000)
    else:
    	display.clear()