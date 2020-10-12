from microbit import * # tell python code will run on micro:bit
display.clear() # makes sure all display LEDs are off
while True:
    pin8.write_digital(1)  # turn Maqueen's left  LED on
    pin12.write_digital(0) # turn Maqueen's right LED off
    sleep(1000) # sleep for 1000 milliseconds = 1 second
    pin8.write_digital(0)  # turn Maqueen's left  LED off
    pin12.write_digital(1) # turh Maqueen's right LED on
    sleep(1000) # sleep for 1000 milliseconds = 1 second