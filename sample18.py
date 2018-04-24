import cv2
import numpy as np

img = cv2.imread("myface.jpeg")


#kernel = np.ones((5,5),np.float32)/35
#dst = cv2.filter2D(img,-1,kernel)

#dst = cv2.blur(img, (10,10))
dst = cv2.GaussianBlur(img, (11,11), 5)

out1 = cv2.Canny(img, 100, 100)
out2 = cv2.Canny(dst, 100, 100)

cv2.imshow("face", img)
cv2.imshow("out", dst)
cv2.imshow("out1", out1)
cv2.imshow("out2", out2)

cv2.waitKey(0)
cv2.destroyAllWindows()
