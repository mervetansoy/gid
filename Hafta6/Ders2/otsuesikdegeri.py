import cv2 as cv
import numpy as np

src = cv.imread("images.jpg")
if src is None:
    print("HATA: images.jpg dosyasi bulunamadi!")
    exit()

cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
print("Otsu esik megeri:", ret)
cv.imshow("binary", binary)

cv.waitKey(0)
cv.destroyAllWindows()