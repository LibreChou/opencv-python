import cv2
import numpy as np

body_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

#cap = cv2.VideoCapture(0)

img = cv2.imread("test1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = body_cascade.detectMultiScale(gray, 1.1, 2)
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imshow("img", img)

k = cv2.waitKey(0)

cv2.destroyAllWindows()

        
    

