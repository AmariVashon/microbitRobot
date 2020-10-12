from microbit import * # tell python code will run on micro:bit
# variables useful for motor control:
ADDR_MOTOR_CNTRL 	= 16 # I2C address of the motor control chip
DIR_FORWARD         = 0 # forward direction specification
DIR_BACKWARD        = 1 # backward direction specification

# motor move command
# i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_LEFT,speed_left,DIR_RIGHT,speed_right]))

# make the robot move forward
speed = 125 # speed must be between 0 and 255 inclusive
i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_FORWARD,speed,DIR_FORWARD,speed]))
# let robot move for 2 seconds
sleep(2000)
# stop the robot
speed = 0 # speed must be between 0 and 255 inclusive
i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_FORWARD,speed,DIR_FORWARD,speed]))
# the above instruction is the same as typing:
# i2c.write(16,bytearray([0,0,0,0,0]))
# wait for two seconds
sleep(2000)

# drive backward
speed = 125 # speed must be between 0 and 255 inclusive
i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_BACKWARD,speed,DIR_BACKWARD,speed]))
# let robot move for 2 seconds
sleep(2000)
# stop the robot
speed = 0 # speed must be between 0 and 255 inclusive
i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_FORWARD,speed,DIR_FORWARD,speed]))
