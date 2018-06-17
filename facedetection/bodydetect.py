import cv2
import numpy as np

body_cascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    if ret == True:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = body_cascade.detectMultiScale(gray, 1.1, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

        cv2.imshow("img", img)

    k = cv2.waitKey(30)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

        
    

