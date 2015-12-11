"""
	Python script for using firmata to communicate with an arduino.
	We elect to use firmata here because it can trigger a pololu driver
        on the arduino to drive the face of Marie Curie.

	This script will be called by the power point once the user presses a button.

	Programmed by William Harrington
	ECE478 Final Project
"""

# use python firmata package
import pyfirmata

# use time package for delay
import time

# use pin 8
PIN = 8

# this needs to be changed according to the port you have plugged in
PORT = '\\.\COM9'

# initialize variable for changing behavior
last = 0

# variable for current time
time2 = 0

# declare board
board = pyfirmata.Arduino(PORT)

# loop for making marie curie's face move
for i in range(4):

    # grab current time
    time2 = time.strftime('%H:%M:%S')

    # show current time and current loop
    print '%s: On loop %s' % (time2, i)

    # write the pin on the board to the value last
    board.digital[PIN].write(last)

    # invert last
    last = not last

    # delay 3 seconds
    time.sleep(3)

board.digital[PIN].write(0)
time.sleep(7)
PIN = 9
last = 0

# loop for making marie curie's face smil
for i in range(4):

    # grab current time
    time2 = time.strftime('%H:%M:%S')

    # show current time and current loop
    print '%s: On loop %s' % (time2, i)

    # write the pin on the board to the value last
    board.digital[PIN].write(last)

    # invert last
    last = not last

    # delay 3 seconds
    time.sleep(3)

# pull pin low, exit out
board.digital[PIN].write(0)
board.exit()
