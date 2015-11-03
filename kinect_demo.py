from SimpleCV import *

kin = Kinect()
#display = kin.getDepth().show()
display = kin.getImage().show()
while True:
    #depth = kin.getDepth()
    #depth.save(display)
    img = kin.getImage()
    img.save(display)
