from microbit import *
from random import *

image1 = Image( "00000:"
                "00000:"
                "00900:"
                "00000:"
                "00000:")
                
image2 = Image( "00009:"
                "00000:"
                "00000:"
                "00000:"
                "90000:")
                
image3 = Image( "00009:"
                "00000:"
                "00900:"
                "00000:"
                "90000:")
                
image4 = Image( "90009:"
                "00000:"
                "00000:"
                "00000:"
                "90009:")
                
image5 = Image( "90009:"
                "00000:"
                "00900:"
                "00000:"
                "90009:")
                
image6 = Image( "90009:"
                "00000:"
                "90009:"
                "00000:"
                "90009:")                

while True:
    if accelerometer.was_gesture("shake"):
        value = randint(1,6)
        if value == 1:
            display.show(image1)
        elif value == 2:
            display.show(image2)
        elif value == 3:
            display.show(image3)
        elif value == 4:
            display.show(image4)
        elif value == 5:
            display.show(image5)
        else:
            display.show(image6)
        sleep(2000)
    else:
        display.clear()
