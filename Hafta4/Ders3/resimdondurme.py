import cv2 as cv
import numpy as np

img = cv.imread("images.jpg")

rows = img.shape[0]
cols = img.shape[1]

M = cv.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)

rotated = cv.warpAffine(img, M, (cols, rows))

cv.imshow("Dondurulmus", rotated)

cv.waitKey(0)
cv.destroyAllWindows()
