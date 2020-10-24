from microbit import * # import Micro:Bit module

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
    
# demonstrate commands
forward(200) 	# drive forward at speed 200/255
sleep(2000)  	# let drive forward command run for 2 seconds
stop()   		# stop moving
sleep(1000) 	# allow 1 second for robot to stop
turnRight(100)  # veer to the right at speed 100/255
sleep(1000)	 	# allow turn command to run for 1 second
forward(200) 	# drive forward at speed 200/255
sleep(1000)  	# let drive forward command run for 1 second
stop() 			# stop robot
sleep(1000) 	# allow 1 second for robot to stop
backward(80) 	# drive backward at speed 80/255
sleep(1000)     # drive backward for 1 second
stop()   		# stop moving