import cv2
import numpy as np

cap = cv2.VideoCapture(0)

fps = int(cap.get(cv2.CAP_PROP_FPS))
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 24, (w, h), False)
print (fps, w, h)

while True:
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(gray)
        cv2.imshow("video", gray)
        if((cv2.waitKey(1) & 0xFF) == ord('q')):
           break

out.release()
cap.release()
cv2.destroyAllWindows()
