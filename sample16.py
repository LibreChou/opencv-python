import cv2
import numpy as np

img = cv2.imread("myface.jpeg")


#pts1 = np.float32([[50,50],[200,50],[50,200]])
#pts2 = np.float32([[10,100],[200,50],[100,250]])

pts1 = np.float32([[0,0],[200,50],[50,200]])
pts2 = np.float32([[0,0],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(640,480))

cv2.imshow("face", img)
cv2.imshow("out", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
