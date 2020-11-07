from microbit import *
import radio

# variables useful for motor control:
ADDR_MOTOR_CNTRL    = 16 # motor control chip's I2C address    

# Note: the robot needs to have batteries and be turned on for the 
# i2c.write(ADDR_MOTOR_CNTRL,...) command to work!!!!

# set up radio
radio.config(channel=19) # channel can be 0 to 83 inclusive
radio.config(power=7)    # power can be 0 (min) to 7 (max), 6 is default
radio.on()

def directBothWheels(dir_left,spd_left,dir_right,spd_right):
	# direct control over both wheels
	# ---- input ----
	# dir_left: 0 to go forward, 1 to go backward
	# spd_left: motor spin speed.  0 is stopped, 255 is max speed.
	# dir_right: 0 to go forward, 1 to go backward
	# spd_right: motor spin speed.  0 is stopped, 255 is max speed.
	i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,dir_left,spd_left,dir_right,spd_right]))
	
while True:
    # read from radio
    incoming = radio.receive_bytes()
    
    # only process messages that aren't empty
    if incoming is not None:
        # process messages 
        dir_left    = incoming[0]
        spd_left    = incoming[1]
        dir_right   = incoming[2]
        spd_right   = incoming[3]
        # send new motor command
        directBothWheels(dir_left,spd_left,dir_right,spd_right)