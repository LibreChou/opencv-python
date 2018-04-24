import cv2
import numpy as np

img = cv2.imread("myface.jpeg")

b,g,r = cv2.split(img)

cv2.imshow("face", img)

cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)

cv2.waitKey(0)
cv2.destroyAllWindows()
