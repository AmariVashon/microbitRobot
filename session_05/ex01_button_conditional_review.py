from microbit import *
while True:
    if button_a.is_pressed()==True:
        display.scroll("A")
    if button_b.is_pressed()==True:
        display.scroll("B")