


import numpy as np
import cv2

from pyzbar import pyzbar


cap = cv2.VideoCapture(-1)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, image = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    
    barcodes = pyzbar.decode(gray)
    for barcode in barcodes:
        print("")
        
        # Get the rect/contour coordinates:
        left = barcode.rect[0]
        top = barcode.rect[1]
        width = barcode.rect[2]
        height = barcode.rect[3]
        print(f'left={left},top={top},width={width},height={height}')

        # get the rectangular contour corner coordinates
        top_left = [top,left]
        print(f'top_left={top_left}')
        top_right = [top,left+width]
        print(f'top_right={top_right}')
        bottom_left = [top-height,left]
        print(f'bottom_left={bottom_left}')
        bottom_right = [top-height,left+width]
        print(f'bottom_right={bottom_right}')
        
        (x,y,w,h) = barcode.rect
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 2)
        
        cv2.circle(image, barcode.polygon[0], 2, (0,255,0), 2)
        cv2.circle(image, barcode.polygon[1], 2, (0,255,255), 2)
        cv2.circle(image, barcode.polygon[2], 2, (255,0,255), 2)
        cv2.circle(image, barcode.polygon[3], 2, (255,255,0), 2)
        
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
    
    
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image,text,(x,y-10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0,0,255), 2)
        print ("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
    
    # Display the resulting frame
    cv2.imshow('frame', image);
    if cv2.waitKey(1) == ord('q'):
        break
        

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

