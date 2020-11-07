from microbit import *

# map function (shamelessly copied from arduino library) 
# https://www.arduino.cc/reference/en/language/functions/math/map/
def map(x,in_min,in_max,out_min,out_max):
    return round(out_min + (x-in_min)*(out_max-out_min)/(in_max-in_min))

while True:
    # read joystick position
    joy_x = pin1.read_analog()
    joy_y = pin2.read_analog()
    # linearly interpolate (x,y) range from [0,1023] to [0,5]
    x_disp = map(joy_x,0,1023,0,4)
    y_disp = map(joy_y,0,1023,4,0)
    # update display
    display.clear()
    display.set_pixel(x_disp,y_disp,9)