import cv2
import numpy as np

img = cv2.imread("myface.jpeg")

cols = 640
rows = 480

M = cv2.getRotationMatrix2D((cols/2,rows/2),120,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow("face", img)
cv2.imshow("out", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
