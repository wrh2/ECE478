from SimpleCV import Kinect
import time
kin = Kinect()
img = kin.getImage()
img.show()
time.sleep(5)
