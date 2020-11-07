from microbit import *
while True:
    joy_x = pin1.read_analog()
    joy_y = pin2.read_analog()
    display.scroll(joy_x)
    display.scroll(',')
    display.scroll(joy_y)
    sleep(1000)