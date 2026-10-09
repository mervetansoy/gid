import cv2 as cv
import numpy as np

src = cv.imread("res1.jpg")
cv.imshow("Orijinal Goruntu", src)

dst5 = cv.bitwise_not(src)
cv.imshow("NOT Sonucu", dst5)

cv.waitKey(0)
cv.destroyAllWindows()