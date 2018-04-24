import cv2
import numpy as np

img1 = cv2.imread("myface.jpeg")
img2 = cv2.imread("track.jpg")

img = cv2.bitwise_not(img1)

out = cv2.bitwise_and(img1, img, img)

cv2.imshow("face", img)
cv2.imshow("out", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
