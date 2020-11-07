from microbit import *
import radio

# set up radio
radio.config(channel=19) # channel can be 0 to 83 inclusive
radio.config(power=7)    # power can be 0 (min) to 7 (max), 6 is default
radio.on()

while True:
    # read from radio
    incoming = radio.receive_bytes()
    
    # only process messages that aren't empty
    if incoming is not None:
        display.scroll(incoming[0])
        display.scroll(incoming[1])
        display.scroll(incoming[2])
        display.scroll(incoming[3])