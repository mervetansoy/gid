import cv2 as cv
import numpy as np

img = cv.imread("images.jpg")

rows = img.shape[0]
cols = img.shape[1]

res = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
cv.imshow("Kucultulmus", res)

cv.waitKey(0)
cv.destroyAllWindows()
