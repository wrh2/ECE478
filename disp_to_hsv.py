from SimpleCV import *
import time
cam = Camera()
disp = Display()

showEffects = False

def bin(img):
    numpyImg = img.getNumpyCv2()
    hsvValues = img.toHSV().getNumpyCv2()
    hValues = hsvValues[:,:,0]
    hueThreshold = 50
    black = (0,0,0)
    numpyImg[hValues < hueThreshold] = black
    img = Image(numpyImg)
    return img

while disp.isNotDone():
    img = cam.getImage()
    #img = img.grayscale()
    #img = img.flipHorizontal()
    if showEffects:
        img = bin(img)
    if disp.mouseLeft:
        time.sleep(.1)
        showEffects = not showEffects
    img.save(disp)
