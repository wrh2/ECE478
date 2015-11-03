from SimpleCV import *
import time

kin = Kinect()
display = kin.getDepth().show()
while True:
    dep = kin.getDepth()
    img = kin.getImage()
    fore = dep.binarize(190)#.invert()
    fore_only = img - fore
    fore_only.save(display)
