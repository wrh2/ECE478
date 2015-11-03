from SimpleCV import *

cam = Kinect()
rs = RunningSegmentation(.5)

size = (cam.getImage().size())
disp = cam.getImage().show()

center = (size[0] / 2, size[1] / 2)

while True:
    input = cam.getImage()
    input = input.flipHorizontal()
    rs.addImage(input)

    if disp.mouseLeft:
        break

    if(rs.isReady()):
        img = rs.getSegmentedImage(False)
        blobs = img.dilate(3).findBlobs()

        if(blobs is not None):
            blobs = blobs.sortArea()
            center = (int(blobs[-1].minRectX()),
                      int(blobs[-1].minRectY()))
        input.dl().circle(center, 50, Color.BLACK, width = 3)
        input.dl().circle(center, 200, Color.BLACK, width = 6)
        input.drawText("Object located at: %d, %d" % (center[0], center[1]), 0,0, fontsize=60, color=Color.YELLOW)
        input.dl().line((center[0], center[1] - 50), (center[0], 0), Color.BLACK, width = 2)
        input.dl().line((center[0], center[1] + 50), (center[0], size[1]), Color.BLACK, width = 2)
        input.dl().line((center[0] - 50, center[1]), (0, center[1]), Color.BLACK, width = 2)
        input.dl().line((center[0] + 50, center[1]), (size[0], center[1]), Color.BLACK, width = 2)
        input.save(disp)
