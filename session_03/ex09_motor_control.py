from microbit import * # import Micro:Bit module

# variables useful for motor control:
ADDR_MOTOR_CNTRL    = 16 # motor control chip's I2C address    
DIR_FORWARD         = 0     # forward direction specification
DIR_BACKWARD        = 1  # backward direction specification

# Note: the robot needs to have batteries and be turned on for the 
# i2c.write(ADDR_MOTOR_CNTRL,...) command to work!!!!

# motor move command
# i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_LEFT,speed_left,DIR_RIGHT,speed_right]))

# make the robot move forward
speed =  125
i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_FORWARD,speed,DIR_FORWARD,speed]))
# let robot move for 2 seconds
sleep(2000)
# stop the robot
speed =  0
i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_FORWARD,speed,DIR_FORWARD,speed]))
# wait for two seconds
sleep(2000)
# drive backward
speed =  125
i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_BACKWARD,speed,DIR_BACKWARD,speed]))
# let robot move for 2 seconds
sleep(2000)
# stop the robot
speed =  0
i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_FORWARD,speed,DIR_FORWARD,speed]))