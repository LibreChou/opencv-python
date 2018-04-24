import cv2
import numpy as np

img = cv2.imread("test.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lg = np.array([174,50,50])
ug = np.array([230, 255, 255])

mask = cv2.inRange(hsv, lg, ug)
res = cv2.bitwise_and(hsv,hsv, mask= mask)

cv2.imshow("mask", mask)
cv2.imshow("hsv", res)
cv2.imwrite("track.jpg", res)

cv2.imshow("face", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
