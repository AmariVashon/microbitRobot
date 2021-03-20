# Uploaded by Amari Harrington

from microbit import *
import radio

# set up radio
radio.config(channel=19) # channel can be 0 to 83 inclusive
radio.config(power=7)    # power can be 0 (min) to 7 (max), 6 is default
radio.on()

# moto:bit address is 0x59 = 0d89
motobit_addr = 0x59 

# moto:bit registers
reg_motor_left      = 0x21
reg_motor_right     = 0x20
reg_motor_enable    = 0x70
motor_enable        = 0x01
motor_disable       = 0x00

# map function (shamelessly copied from arduino library) 
# https://www.arduino.cc/reference/en/language/functions/math/map/
def map(x,in_min,in_max,out_min,out_max):
    return round(out_min + (x-in_min)*(out_max-out_min)/(in_max-in_min))
    
def forward(pwr):
    # spins drive wheels forward 
    # pwr :  motor power.  0 is stopped, 100 is max power.
    # change the user command from range [0 100] to [128 255]
    pwr_cmd = map(pwr,0,100,128,255)
    i2c.write(motobit_addr,bytearray([reg_motor_left,pwr_cmd]))

# set pin 15 to use a pull-up resistor
# since read_digital() defaults to a pull-down resistor
# and we need to use a pull-up resistor to use the hall effect sensor
pin15.set_pull(pin15.PULL_UP)

# enable drive motor
i2c.write(motobit_addr,bytearray([reg_motor_enable,motor_enable]))


prev_hall_meas = 1

ticks = 0

# how far our robot thinks it has driven based on the encoder measurements
distance_traveled = 0

# Ten80 tells us to drive this number of inches
distance_to_travel = 50

# in engineering notebook, we found 1.83 encoder ticks per inch traveled
ticks_per_inch = 1.83
inch_per_tick  = 1/ticks_per_inch


# ten80 robot: set steering to drive straight
# set up the steering servo
pin16.set_analog_period(20)
pin16.write_analog(70) # set pulse width = 72.5/1023 * 20 ms = 1.5 ms

# drive forward slowly
forward(50)


while True:
    hall_meas = pin15.read_digital()
    # check to see if hall effect sensor has changed from 1 to 0
    if (prev_hall_meas == 1) and (hall_meas == 0):
        ticks = ticks + 1
        distance_traveled = ticks*inch_per_tick
        #print(distance_traveled)
        radio.send(str(distance_traveled))
    if distance_traveled >= distance_to_travel:
        # break out of the while loop once our robot has traveled the specified distance
        break
    # prepare for next time through the while loop
    prev_hall_meas = hall_meas
    
# stop once our program has broken out of the while loop
forward(0) 
