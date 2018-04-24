import cv2
import numpy as np

img = cv2.imread("myface.jpeg")

print (img[10,300])
print (img[150, 20])
cv2.imshow("orig", img)

img[10,300, 0] = 255
img[11,300, 0] = 255
img[12,300] = [255,255,0]
img[13,300] = [255,255,0]
img[14,300] = [255,255,0]
img[15,300] = [255,255,0]
img[16,300] = [255,255,0]
img[17,300] = [255,255,0]
img[18,300] = [255,255,0]
img[19,300] = [255,255,0]

print (img.size)
print (img.dtype)
print (img.shape)

cv2.imshow("face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
