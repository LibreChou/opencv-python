import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces = []
labels = []

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 2)
    for(x,y,w,h) in faces:
        return gray[y:y+h, x:x+w]

img = cv2.imread("1.jpg")
face = detect_face(img)

faces.append(face)
labels.append(1)


img = cv2.imread("2.jpg")
face = detect_face(img)

faces.append(face)
labels.append(2)

img = cv2.imread("3.jpg")
face = detect_face(img)

faces.append(face)
labels.append(3)

img = cv2.imread("4.jpg")
face = detect_face(img)

faces.append(face)
labels.append(4)

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.train(faces, np.array(labels))

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 2)
    for(x,y,w,h) in faces:
        face_gray = gray[y:y+h, x:x+w]    
        ret, threshold = recognizer.predict(face_gray)
        print (ret)
        print (threshold)

    cv2.imshow("img", img)
    k = cv2.waitKey(30)
    if k == 30:
        break

cap.release()
cv2.destroyAllWindows()
