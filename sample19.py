import cv2
import numpy as np

img = cv2.imread("myface.jpeg")

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=11)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=11)
laplacian = cv2.Laplacian(img,cv2.CV_64F)
out = cv2.Canny(img, 11, 11)

cv2.imshow("face", img)
cv2.imshow("sx", sobelx)
cv2.imshow("sy", sobely)
cv2.imshow("lap", laplacian)
cv2.imshow("out", out)

cv2.waitKey(0)
cv2.destroyAllWindows()
