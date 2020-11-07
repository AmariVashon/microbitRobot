from microbit import *

while True:
    # read GamePad's programmable buttons 
    if pin13.read_digital() == 0:
        display.scroll("Grn")
        pin13.write_digital(1)
    if pin14.read_digital() == 0:
        display.scroll("Yel")
        pin14.write_digital(1)
    if pin15.read_digital() == 0:
        display.scroll("Red")
        pin15.write_digital(1)
    if pin16.read_digital() == 0:
        display.scroll("Blu")
        pin16.write_digital(1)
        
    # read GamePad's joystick push button    
    if pin8.read_digital() == 0:
        display.scroll("J")
        pin8.write_digital(1)

    # read GamePad's trigger buttons (wired to Micro:Bit's A and B buttons)
    if pin5.read_digital() == 0:
        display.scroll("A")
    if pin11.read_digital() == 0:
        display.scroll("B")