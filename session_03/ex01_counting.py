from microbit import *
count = 0 # a variable to store the current count
while True:
    display.scroll(count) # show the current count on the display
    count = count + 1 # each time through the loop, increase count
    sleep(1000) # pause for a second
