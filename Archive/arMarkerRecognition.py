#############################################################
### This file was archived after many better functions were
### found. It is still useful to show how to manage the
### detectMarker return arrays without the classes I later
### set up.
#############################################################

import cv2 as cv
import numpy as np

# Find attached camera
cap = cv.VideoCapture(-1)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

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

    # Detect the markers in the image
    markerCorners, markerIds, rejectedCandidates = cv.aruco.detectMarkers(frame, dictionary, parameters=parameters)

    #for marker in markerCorners[0][0]
    if(markerCorners != [] or markerIds != None):
        for i in range(0,len(markerCorners)):
            x = int(markerCorners[i][0][0][0])
            y = int(markerCorners[i][0][0][1])
            cv.circle(frame, (x,y), 2, (0,255,0), 2)
            
            x = int(markerCorners[i][0][2][0])
            y = int(markerCorners[i][0][2][1])
            
            cv.circle(frame, (x,y), 2, (255,0,0), 2)
            text = str(markerIds[i][0])
            cv.putText(frame,text,(x,y-10), cv.FONT_HERSHEY_SIMPLEX,
                    0.5, (0,0,255), 2)
            print("Found marker " + text)
            print("Top corner at " + str(x) + ", " + str(y))
        print("")
    
    # Display the resulting frame
    cv.imshow('frame', frame);
    if cv.waitKey(1) == ord('q'):
        break
    
    
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
