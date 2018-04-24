import cv2
import numpy as np

img = cv2.imread("myface.jpeg")

cv2.line(img, (10,10), (200,200), (255, 0, 0), 5)
cv2.rectangle(img, (20,20), (150,150), (0, 255,0), -1)
cv2.circle(img, (25,25), 20, (0,0,255), 5)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
cv2.polylines(img, [pts], True, (255,255,255), 10)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Neevee", (200,200), font, 5, (255,255,255), 3, cv2.LINE_AA)

cv2.imshow("face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
