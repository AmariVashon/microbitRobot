from microbit import * # import Micro:Bit module

# This program is designed for a DFRobot Micro Maqueen Lite robot to drive 
# on a DFRobot Track Map-V1.0.
#
# The DFRobot Track Map-V1.0 is white with a wide black path/track
#
# The DFRobot Micro Maqueen Lite robot has two infrared reflectance sensors (IR sensors).
# The IR sensors are positioned close enough together to both see black when the robot
# drives over the center of the wide black path/track.

# variables useful for motor control:
ADDR_MOTOR_CNTRL    = 16 # motor control chip's I2C address    
DIR_FORWARD         = 0  # forward direction specification
DIR_BACKWARD        = 1  # backward direction specification

# Note: the robot needs to have batteries and be turned on for the 
# i2c.write(ADDR_MOTOR_CNTRL,...) command to work!!!!

# motor move command
# i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_LEFT,speed_left,DIR_RIGHT,speed_right]))

def forward(speed):
	# spins both wheels forward at the same speed
	# speed : byte, motor spin speed.  0 is stopped, 255 is max speed.
	i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_FORWARD,speed,DIR_FORWARD,speed]))

def backward(speed):
	# spins both wheels backward at the same speed
	# speed : byte, motor spin speed.  0 is stopped, 255 is max speed.
	i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_BACKWARD,speed,DIR_BACKWARD,speed]))
    
def turnRight(speed):
	# spins left wheel forward to turn robot to its right
	# speed : byte, motor spin speed.  0 is stopped, 255 is max speed.
	i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_FORWARD,speed,DIR_FORWARD,0]))

def turnLeft(speed):
	# spins right wheel forward to turn robot to its left
	# speed : byte, motor spin speed.  0 is stopped, 255 is max speed.
	i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_FORWARD,0,DIR_FORWARD,speed]))

def stop():
	# stops both drive motors
	i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,0,0,0,0]))


def line_sensor_left():
    # reads left line sensor
    # outputs 0 (False) over absorptive (dark) surface, 1 (True) over reflective (bright) surface
    return pin13.read_digital()
    
def line_sensor_right():
    # reads right line sensor
    # outputs 0 (False) over absorptive (dark) surface, 1 (True) over reflective (bright) surface
    return pin14.read_digital()
    
while True:
    # read both line sensors ONCE each time through while loop
    # line sensor functions return True (if they see white) or False (if they see a line)
    line_is_under_left_sensor  = not line_sensor_left()
    line_is_under_right_sensor = not line_sensor_right()
    
    if (line_is_under_left_sensor == True) and (line_is_under_right_sensor == True):
        # line is under both sensors.  go forward.
        forward(25)
    elif (line_is_under_left_sensor == False) and (line_is_under_right_sensor == True):
        # line only under right sensor.  need to turn right.
        turnRight(25)
    elif (line_is_under_left_sensor == True) and (line_is_under_right_sensor == False):
        # line only under left sensor.  need to turn left.
        turnLeft(25)
    else:
        # line not found!  go forward to look for a line.
        forward(25)	