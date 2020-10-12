from microbit import * # tell python code will run on micro:bit
# variables useful for motor control:
ADDR_MOTOR_CNTRL    = 16 # I2C address of the motor control chip
DIR_FORWARD         = 0 # forward direction specification
DIR_BACKWARD        = 1 # backward direction specification


def forward(speed=125):
    # spins both wheels forward at the same speed
    # speed : byte, optional. motor spin speed.  0 is stopped, 255 is max speed
    i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_FORWARD,speed,DIR_FORWARD,speed]))

def backward(speed=125):
    # spins both wheels backward at the same speed
    # speed : byte, optional. motor spin speed.  0 is stopped, 255 is max speed
    i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_BACKWARD,speed,DIR_BACKWARD,speed]))

def turnRight(speed=125):
    # spins left wheel forward while right wheel is stopped
    # speed : byte, optional.  motor spin speed.  0 is stopped, 255 is max speed
    i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_FORWARD,speed,DIR_FORWARD,0]))

def turnLeft(speed=125):
    # spins right wheel forward while left wheel is stopped
    # speed : byte, optional.  motor spin speed.  0 is stopped, 255 is max speed
    i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_FORWARD,0,DIR_FORWARD,speed]))

def stop():
    # stop both drive motors
    i2c.write(ADDR_MOTOR_CNTRL,bytearray([0,DIR_FORWARD,0,DIR_FORWARD,0]))


# demonstrate our new functions!!!
forward(200)    # drive forward at speed 200/255
sleep(5000)     # keep driving for 5 seconds
stop()          # stop moving
sleep(1000)     # allow robot to come to a stop
turnRight(100)  # veer to the right at speed 100/255
sleep(1000)     # allow robot to turn for 1 second
stop()