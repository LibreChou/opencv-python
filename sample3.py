import cv2
import numpy as np

cap = cv2.VideoCapture('cvtest.mp4')

fps = int(cap.get(cv2.CAP_PROP_FPS))
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))
print (fps, w, h)

while True:
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        cv2.imshow("video", frame)
        if((cv2.waitKey(1) & 0xFF) == ord('q')):
           break

out.release()
cap.release()
cv2.destroyAllWindows()
