import cv2
import numpy as np

img = cv2.imread("myface.jpeg")

b,g,r = cv2.split(img)

img[:,:,0] = 0
img[:,:,2] = 0

cv2.imshow("face", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
