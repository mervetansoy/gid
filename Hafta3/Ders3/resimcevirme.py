import cv2 as cv
import numpy as np

src = cv.imread("res.jpg")
cv.imshow("Orijinal Goruntu", src)
cv.waitKey(1)

dst1 = cv.flip(src, 0)
cv.imshow("X Flip", dst1)
cv.waitKey(1)

dst2 = cv.flip(src, 1)
cv.imshow("Y Flip", dst2)
cv.waitKey(1)

dst3 = cv.flip(src, -1)
cv.imshow("X-Y Flip", dst3)
cv.waitKey(1)

cv.waitKey(0)
cv.destroyAllWindows()