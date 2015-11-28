from SimpleCV import Camera, Display
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
out = False
GPIO.output(12, out)

threshold = 5.0

cam = Camera()
previous = cam.getImage()

disp = Display(previous.size())

while not disp.isDone():
    current = cam.getImage()
    diff = current - previous

    matrix = diff.getNumpy()
    mean = matrix.mean()

    diff.save(disp)

    if mean >= threshold:
        print "Motion Detected"
        out = True
    else:
        out = False

    GPIO.output(12, out)
    time.sleep(.1)
    previous = current
