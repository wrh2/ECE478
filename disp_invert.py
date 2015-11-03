from SimpleCV import *
cam = Camera()
disp = Display()

while disp.isNotDone():
    img = cam.getImage()
    img = img.flipHorizontal()
    img = img.invert()
    #img = img.toHSV()
    if disp.mouseLeft:
        break
    img.save(disp)
