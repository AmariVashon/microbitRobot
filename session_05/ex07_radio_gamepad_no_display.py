from microbit import *
import radio

# set up radio
radio.config(channel=19) # channel can be 0 to 83 inclusive
radio.config(power=7)    # power can be 0 (min) to 7 (max), 6 is default
radio.on()

# message buffer to send to robot
message = bytearray([0,0,0,0])

# forward and backward direction definitions for robot's motor controller
DIR_FORWARD     = 0    
DIR_BACKWARD    = 1     

# map function (shamelessly copied from arduino library) 
# https://www.arduino.cc/reference/en/language/functions/math/map/
def map(x,in_min,in_max,out_min,out_max):
    return round(out_min + (x-in_min)*(out_max-out_min)/(in_max-in_min))

while True:
    # read joystick position
    # read_analog returns a number in range [0,1023]
    joy_x   = pin1.read_analog()
    joy_y   = pin2.read_analog()
    # convert range to [-512,511]
    x       = joy_x - 512
    y       = joy_y - 512
    # implement deadzone since joysticks aren't exact
    # treat any joystick measurements NEAR center as if they are AT center
    if x > -30 and x < 30:
        x = 0
    if y > -30 and y < 30:
        y = 0

    # arcade style steering
    signed_spd_left   = y + x
    signed_spd_right  = y - x

    # convert to motor command arguments
    if signed_spd_left >= 0:
        dir_left = DIR_FORWARD
        spd_left = map(signed_spd_left,0,511,0,255)
    else:
        dir_left = DIR_BACKWARD
        spd_left = map(signed_spd_left,-512,0,255,0)
    # also convert right motor command
    if signed_spd_right >= 0:
        dir_right = DIR_FORWARD
        spd_right = map(signed_spd_right,0,511,0,255)
    else:
        dir_right = DIR_BACKWARD
        spd_right = map(signed_spd_right,-512,0,255,0)

    # load motor command arguments into buffer
    message[0] = dir_left
    message[1] = spd_left
    message[2] = dir_right
    message[3] = spd_right
    # send the buffered message out via radio
    radio.send_bytes(message)