import cv2 as cv
import numpy as np

src = cv.imread("test.png")

if src is None:
    print("HATA: test.png dosyasi bulunamadi!")
    exit()

cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(1)

h, w = src.shape[:2]

dst = cv.bilateralFilter(src, 0, 50, 10)

result = np.zeros((h, w * 2, 3), dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w:w * 2, :] = dst

cv.imshow("Orijinal ve Filtrelenmis", result)

cv.waitKey(0)
cv.destroyAllWindows()