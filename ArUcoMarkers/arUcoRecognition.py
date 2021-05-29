import cv2 as cv
import numpy as np
from math import sqrt

# These classes just make handling the return of detectMarkers
# easier to manage
class Marker:
    def __init__(self, i,markerCorners, markerIds):
        self.top_left =     Point(int(markerCorners[i][0][0][0]), int(markerCorners[i][0][0][1]))
        self.top_right =    Point(int(markerCorners[i][0][1][0]), int(markerCorners[i][0][1][1]))
        self.bottom_right = Point(int(markerCorners[i][0][2][0]), int(markerCorners[i][0][2][1]))
        self.bottom_left =  Point(int(markerCorners[i][0][3][0]), int(markerCorners[i][0][3][1]))
        
        self.id = int(markerIds[i][0])
        
    def formArray (self):
        return [[self.top_left.x,self.top_left.y],
         [self.top_right.x,self.top_right.y],
         [self.bottom_right.x,self.bottom_right.y],
         [self.bottom_left.x,self.bottom_left.y]]        
        
        
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


# Find attached camera
cap = cv.VideoCapture(-1)

if not cap.isOpened():
    print("Cannot open camera")
    exit()


## https://learnopencv.com/augmented-reality-using-aruco-markers-in-opencv-c-python/
    
# Load the predefined dictionary
dictionary = cv.aruco.Dictionary_get(cv.aruco.DICT_6X6_250)

# Initialize the detector parameters using default values
parameters =  cv.aruco.DetectorParameters_create()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    markerIds = []
    # Detect the markers in the image
    markerCorners, markerIds, rejectedCandidates = cv.aruco.detectMarkers(frame, dictionary, parameters=parameters)

    # draw borders and id numbers around markers
    ### This step was orginally done by hand before this function was discovered
    ### Find That in Archive/ArUcoRecognition.py
    cv.aruco.drawDetectedMarkers(frame, markerCorners,markerIds)
    
    markers = []
    ### This portion shows how to manage markers
    # Check if there are any markers in the frame
    if(markerCorners != [] or markerIds != None):
        
        # Loop through every avaliable marker
        for i in range(0,len(markerCorners)):
            # create object, passing in the index of this marker, the array of
            #   corner postions and the array of ids.
            ### Object was used to avoid painful arrays created by detectMarkers
            marker = Marker(i,markerCorners,markerIds)
            ### f strings are magical
            print(f"Found marker {marker.id}")
            markers.append(marker)
        
        if (len(markers) > 1):
            # m1.tl + (m1.tl - m0.tl)
            x = markers[1].top_left.x + (markers[1].top_left.x - markers[0].top_left.x)
            y = markers[1].top_left.y + (markers[1].top_left.y - markers[0].top_left.y)
            ### cv.(shape) draws lots of shapes. This is useful for simple graphics
            # Create dot (frame, dot position, radius, color, border thickness = -1)
            cv.circle(frame, (x,y), 2, [255,0,255], -1)
                    
        print("")
    
        
    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
    
    
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
