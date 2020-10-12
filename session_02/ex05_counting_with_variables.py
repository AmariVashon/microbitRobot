from microbit import * # tell python code will run on micro:bit
count = 0 # a variable to store the current count
while True:
	count = count + 1 # each time through the loop, increase count
	display.scroll(count) # show the count on the display
	sleep(1000) # wait a second