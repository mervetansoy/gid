import cv2 as cv
import numpy as np

img = cv.imread("images.jpg")
rows = img.shape[0]
cols = img.shape[1]

M = np.float32([[1, 0, 300], [0, 1, 90]])

shifted = cv.warpAffine(img, M, (cols, rows))

cv.imshow("Orijinal", img)
cv.imshow("Kaydirilmis", shifted)

cv.waitKey(0)
cv.destroyAllWindows()
