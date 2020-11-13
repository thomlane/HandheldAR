from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.stop_preview()