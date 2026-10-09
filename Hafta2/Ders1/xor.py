import cv2 as cv
import numpy as np

src1 = np.zeros(shape=[400, 400, 3], dtype=np.uint8)
src1[100:200, 100:200, 0] = 255
src1[100:200, 100:200, 2] = 255
cv.imshow("Resim 1", src1)

src2 = np.zeros(shape=[400, 400, 3], dtype=np.uint8)
src2[150:250, 150:250, 2] = 255
cv.imshow("Resim 2", src2)

dst3 = cv.bitwise_xor(src1, src2)
cv.imshow("XOR Sonucu", dst3)

cv.waitKey(0)
cv.destroyAllWindows()