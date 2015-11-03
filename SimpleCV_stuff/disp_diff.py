from SimpleCV import Camera, Display
import time

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

    time.sleep(.1)
    previous = current
