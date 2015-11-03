from SimpleCV import Camera, Color, DiffSegmentation, Display
import time

cam = Camera()
firstImg = cam.getImage()

ds = DiffSegmentation()
ds.addImage(firstImg)

disp = Display(firstImg.size())

showEffects = False

while disp.isNotDone():
    img = cam.getImage()

    if disp.mouseLeft:
        time.sleep(.1)
        showEffects = not showEffects

    if showEffects:
        ds.addImage(img)

        diffImg = ds.getSegmentedImage(False)

        if diffImg is not None:
            blobs = diffImg.dilate(3).findBlobs()
            if(blobs is not None):
                img.dl().polygon(blobs[-1].mConvexHull, color=Color.RED)
