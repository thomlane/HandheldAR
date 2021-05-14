# HandheldAR

OpenCV 4.5.0

Python 3.7.3

## Open CV Installation
Follow the tutorial at:
https://pimylifeup.com/raspberry-pi-opencv/

## Files
#### QR Recognition
Beginning of the project. Recognizes qr codes but cannot orient the marker

#### ArCuo (Should be spelled ArUco; will fix)
A folder of two files.
arMarkerWrite.py takes in one argument, the id of marker. It will then produce a folder called markers in the same location as this file.
arMarkerRecognition.py activates the Pi's camera and start searching for markers in the frame. After finding a marker it will highlights the top left and bottom right corners. The marker's ID will also be printed in the marker's bottom right corner.                             
