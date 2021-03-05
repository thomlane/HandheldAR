import cv2 as cv
import numpy as np
import argparse

# create parser
parser = argparse.ArgumentParser()

#add arguments to the parser
parser.add_argument("id")

#parse arguments
args = parser.parse_args()

# Load the predefined dictionary
dictionary = cv.aruco.Dictionary_get(cv.aruco.DICT_6X6_250)

# Generate the marker
markerImage = np.zeros((200, 200), dtype=np.uint8)
markerImage = cv.aruco.drawMarker(dictionary, int(args.id), 200, markerImage, 1);

cv.imwrite("markers/marker" + str(args.id) + ".png", markerImage);
