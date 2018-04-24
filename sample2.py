import cv2
import numpy as np

cap = cv2.VideoCapture('cvtest.mp4')
while True:
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("video", frame)
        if((cv2.waitKey(1) & 0xFF) == ord('q')):
           break

cap.release()
cv2.destroyAllWindows()
