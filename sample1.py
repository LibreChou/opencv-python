import cv2
import numpy as np

img = cv2.imread("gray.png", cv2.IMREAD_UNCHANGED)

print (img[0,0])

cv2.imshow("face", img)

#cv2.imwrite("gray.png", img)
cv2.waitKey(0)

cv2.destroyAllWindows()
