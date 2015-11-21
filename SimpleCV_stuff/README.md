# Computer vision code in Python

The code currently in this repository makes use of computer vision in python, using some awesome open source software called SimpleCV.
Most of it is experimental and will eventually be incorporated into one of the robots at the PSU Robotics Theatre.

## Dependencies

All code makes use of [SimpleCV] (http://simplecv.org)

In order to use code that involves a kinect, you will need [libfreenect] (http://openkinect.org). This is an open source driver for the kinect. Many operating systems have a way to install this driver as a package.

For example, on Mac OSX with homebrew:
    brew install libfreenect

On linux with apt-get:
   apt-get install freenect

There are detailed instructions on how to install this driver [here] (http://openkinect.org/wiki/Getting_Started).

Official git repo for this driver [here] (http://github.com/OpenKinect/libfreenect).

## Raspberry Pi

As part of my effort to integrate this software with a robot, I have purchased a raspberry pi 2 and installed all dependencies on it. The raspberry pi 2 will a part of whatever robot Dr. Perkowski decides. The useful thing about this is that the raspberry pi can handle the image processing and interface with another device like an Arduino, that is driving a servo controller for instance, via its GPIO pins. This should allow for implementing behavior in the robot based on the image processing.

There is a downside to doing this. Without actually having performed any experiments with this setup, it's hard for me to actually quantify the repercussions. However, it is well known that python itself is 2-100 times slower than C++. This coupled with the heavy load of calculations that come with image processing could make latency a significant problem.

There is also an upside to doing this. The raspberry pi 2 is essentially a computer with GPIO that can be used for doing other things like interfacing with other devices, but its size is a mere fraction of an actual computer. Most robots that I have seen that do image processing with a Kinect require a laptop which takes up a lot of space and makes the robot less mobile. Using a raspberry pi 2, we entirely eliminate this problem. Given a proper housing, the raspberry pi 2 can be set up and placed into the a robot's internal housing. Code can be easily injected into the raspberry pi prior to housing or a wireless module can be used so that code can be implemented remotely. At this time, there is no wireless module on the hardware that I have procured but there may be in the very near future.

If you are looking to get your own raspberry pi set up to do this, all dependencies must be installed. I installed the raspian OS on my raspberry pi and utilized apt-get to obtain the software dependencies. Visit the links in the Dependencies section for more information.

