from picamera import PiCamera
from time import sleep
from datetime import datetime
import numpy

class CameraModule:
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (320, 240)
        self.camera.framerate = 24
        
    def readbuf(self):
        sleep(2)
        image = numpy.empty((240, 320, 3), dtype=numpy.uint8)
        self.camera.capture(image, 'bgr')
        return image

    def capture(self):
        self.camera.start_preview(fullscreen=False, window=(100,20,640,480))
        sleep(3)

        d = datetime.now()
        timename = "/home/pi/Pictures/"
        timename = timename + str(d.year) + str(d.month) + str(d.day) + "_"
        timename = timename + str(d.hour) + str(d.minute) + str(d.second)
        timename = timename + str(d.microsecond) + ".jpg"

        try:
            self.camera.capture(timename)
            print("Capture Saved to \"" + timename + "\"")
        except:
            print("There was an error capturing \"" + timename + "\"!")
    
        self.camera.stop_preview()
        return

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