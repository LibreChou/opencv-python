import cv2
import numpy as np

img = cv2.imread("myface.jpeg")


M = np.float32([[1,0,10],[0,1,100]])
dst = cv2.warpAffine(img,M,(480,640))

cv2.imshow("face", img)
cv2.imshow("out", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
