import cv2 as cv
import numpy as np

img=cv.imread("res.jpg")
cv.namedWindow("Orjinal",cv.WINDOW_AUTOSIZE)
cv.imshow("Orjinal",img)

m1=np.copy(img)
m2 = img

print("img tipi:", type(img))
print("m1 tipi:", type(m1))
print("m2 tipi:",type(m2))

img[100:200, 200:300, :] =255

cv.imshow("Degistilmis",img)
cv.imshow("m1 - bagimsiz kopya",m1)
cv.imshow("m2- referans",m2)

cv.waitKey(0)
cv.destroyAllWindows()