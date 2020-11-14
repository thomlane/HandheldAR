from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()
camera.start_preview(fullscreen=False, window=(100,20,640,480))
sleep(1)

while True:
    userc = input("Input: ")
    
    if (userc == 'q'):
        print("Quitting")
        break
    if (userc == 'c'):
        d = datetime.now()
        timename = "~/Pictures/"
        timename = timename + str(d.year) + str(d.month) + str(d.day) + "_"
        timename = timename + str(d.hour) + str(d.minute) + str(d.second)
        timename = timename + str(d.microsecond) + ".jpg"
        camera.capture(timename)
        print("Capture Saved to \"" + timename + "\"")
    else:
        print("Sorry, input \"" + userc + "\" unrecognisable")
        
camera.stop_preview()