import cv2
import numpy as np

img1 = cv2.imread("myface.jpeg")
img2 = cv2.imread("track.jpg")



out = cv2.Canny(img1, 100, 100)

cv2.imshow("face", img1)
cv2.imshow("out", out)

cv2.waitKey(0)
cv2.destroyAllWindows()
