"""
	Python script for using firmata to communicate with an arduino.
	We elect to use firmata here because it can be used to toggle a pin
	on the arduino. The arduino itself will be running a firmata driver
	along with a pololu driver and some of our own code. Our code
	will simply read pins on the arduino that are encoded to trigger
        the appropriate action when the designated pin is high.

	For example, in the loop section of the arduino code we would do
	something such as
		bool happy = digitalRead(pinNumber)
		if(happy){
			//Trigger pololu to move servos accordingly
		}

	This python code is simply responsible for toggling the pin designated by
	the pseudo variable above called pinNumber. This is the equivalent
	of doing the following in arduino
		digitalWrite(pinNumber, 1)


	Programmed by William Harrington
        ECE478
        Marie Curie Team
        Final Project
"""

# use python firmata package
import pyfirmata

# use time package for delay
import time

# use the sys package for exiting
import sys

# use pin 8
PIN = 8

# this needs to be changed according to the port you have
# the arduino device connected to
# we have ours on the following port, which happens to be
# a windows machine
PORT = '\\.\COM9'

# declare the board
board = pyfirmata.Arduino(PORT)

# value to make pin, note the pins used are digital
# so the values are limited to 0 and 1
value = 1

# debug message
time2 = time.strftime('%H:%M:%S')
print '%s: Toggling pin %s to %s' % (time2, PIN, value)

# now toggle pin
board.digital[PIN].write(value)

# the pin needs to be held at that value
# for a sufficient amount of time in order
# for the appropriate response to happen
time.sleep(2)

# now pull the pin back low
value = not value
board.digital[PIN].write(value)

# let go of serial comm and exit program
board.exit()
sys.exit()
