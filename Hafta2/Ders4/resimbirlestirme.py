import cv2 as cv
import numpy as np

img1 = cv.imread("elma2.jpg")
img2 = cv.imread("elma1.jpg")

cv.imshow("Elma1", img1)
cv.imshow("Elma2", img2)

horizontal = np.hstack((img1, img2))
cv.imshow("Birlestirilmis Goruntu", horizontal)

cv.waitKey(0)
cv.destroyAllWindows()