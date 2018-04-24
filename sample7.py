import cv2
import numpy as np

img = cv2.imread("myface.jpeg")

print (img[10,300])
print (img[150, 20])
f = img[200:350, 250:400]
img[0:150, 0:150] = f

cv2.imshow("face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
