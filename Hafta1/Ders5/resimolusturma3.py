import cv2 as cv
import numpy as np

img = cv.imread("res.jpg")

m1 = np.copy(img)
m2 = img

print("Goruntu boyutu:", img.shape)
print("Goruntu veri tipi:", img.dtype)

img[100:200, 200:300, :] = 0

m3 = np.ones(img.shape, img.dtype) * 255

cv.imshow("m3 - Sifirlardan Olusan Resim", m3)

cv.waitKey(0)
cv.destroyAllWindows()