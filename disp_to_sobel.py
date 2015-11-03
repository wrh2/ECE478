from SimpleCV import *
cam = Camera()
disp = Display()

while disp.isNotDone():
    img = cam.getImage()
    img = img.flipHorizontal()
    img = img.edges()
    #img = img.toHSV()
    if disp.mouseLeft:
        break
    img.save(disp)
