########################################################
# Camera Module
# For Handheld AR
# By Jacob Sowanick
# Using: Python 3.7.3
########################################################
from picamera import PiCamera
from time import sleep
from datetime import datetime
import numpy

# Camera Class, for camera input
class CameraModule:
    def __init__(self):
        self.camera = PiCamera()
        self.camera.framerate = 24
        self.camera.resolution = (1920, 1088)
        self.dimensions = self.camera.resolution
        
    # Changes the dimensions of the camera
    def resize(self, size):
        if (type(size) == type((0,0))):
            self.dimensions = size
            self.camera.resolution = self.dimensions

    # Reads in an image from the camera
    # and returns it as a OpenCV
    # compatible image buffer
    def readbuf(self):
        sleep(2)
        arraysize = (self.dimensions[1], self.dimensions[0], 3)
        image = numpy.empty(arraysize, dtype=numpy.uint8)
        self.camera.capture(image, 'bgr')
        return image

    # Reads in an image after showing a short preview
    # and saves it as a file with current date and time
    def capture(self):
        self.camera.start_preview(fullscreen=False, window=(100,20,640,480))
        sleep(3)

        # This is all to just get the file name
        # which is the current date and time
        d = datetime.now()
        timename = "/home/pi/Pictures/"
        timename = timename + str(d.year) + str(d.month) + str(d.day) + "_"
        timename = timename + str(d.hour) + str(d.minute) + str(d.second)
        timename = timename + str(d.microsecond) + ".jpg"

        # If there is an error, it will handle it, that way
        # we can still stop the preview
        try:
            self.camera.capture(timename)
            print("Capture Saved to \"" + timename + "\"")
        except:
            print("There was an error capturing \"" + timename + "\"!")
    
        self.camera.stop_preview()
        return

    # Run creates an endless loop
    # that the user can use to choose which
    # function you would like to do
    # (quit, capture, read buffer)
    def run(self):
        while True:
            userc = input("Input: ")
    
            if (userc == 'q'):
                print("Quitting")
                return
            elif (userc == 'c'):
                self.capture()
            elif (userc == 'b'):
                self.readbuf()        
            else:
                print("Sorry, input \"" + userc + "\" unrecognisable")