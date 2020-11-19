from picamera import PiCamera
from time import sleep
from datetime import datetime
import numpy

def readbuf():
    camera = PiCamera()
    camera.resolution = (320, 240)
    camera.framerate = 24
    sleep(2)
    image = numpy.empty((240, 320, 3), dtype=numpy.uint8)
    camera.capture(image, 'bgr')
    return image

def capture():
    camera = PiCamera()
    camera.start_preview(fullscreen=False, window=(100,20,640,480))
    sleep(3)

    d = datetime.now()
    timename = "/home/pi/Pictures/"
    timename = timename + str(d.year) + str(d.month) + str(d.day) + "_"
    timename = timename + str(d.hour) + str(d.minute) + str(d.second)
    timename = timename + str(d.microsecond) + ".jpg"

    try:
        camera.capture(timename)
        print("Capture Saved to \"" + timename + "\"")
    except:
        print("There was an error capturing \"" + timename + "\"!")
    
    camera.stop_preview()
    return

def main():
    while True:
        userc = input("Input: ")
    
        if (userc == 'q'):
            print("Quitting")
            return
        elif (userc == 'c'):
            capture()
        elif (userc == 'b'):
            readbuf()        
        else:
            print("Sorry, input \"" + userc + "\" unrecognisable")

main()