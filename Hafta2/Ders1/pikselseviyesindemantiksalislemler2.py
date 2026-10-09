import cv2 as cv
import numpy as np

src1 = np.zeros(shape=[400, 400, 3], dtype=np.uint8)
src1[100:200, 100:200, 1] = 255
src1[100:200, 100:200, 2] = 255
cv.imshow("Resim 1", src1)

src2 = np.zeros(shape=[400, 400, 3], dtype=np.uint8)
src2[150:250, 150:250, 2] = 255
cv.imshow("Resim 2", src2)

dst1 = cv.bitwise_and(src1, src2)
cv.imshow("AND Sonucu", dst1)

cv.waitKey(0)
cv.destroyAllWindows()