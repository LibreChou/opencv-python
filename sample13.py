import cv2
import numpy as np

img = cv2.imread("myface.jpeg")




out = cv2.resize(img, None, fx =1.5, fy =1.5, interpolation = cv2.INTER_CUBIC)

cv2.imshow("face", img)
cv2.imshow("out", out)

cv2.waitKey(0)
cv2.destroyAllWindows()
