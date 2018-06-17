import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    if ret == True:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 5, 0, (100,100), (500,500))
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

            gray_face = gray[y:y+h, x:x+w]
            face_color = img[y:y+h, x:x+w]
            
            eyes = eye_cascade.detectMultiScale(gray_face, 1.1, 2)
            for(ex,ey,ew,eh) in eyes:
                cv2.rectangle(face_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)

        cv2.imshow("img", img)

    k = cv2.waitKey(30)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

        
    

