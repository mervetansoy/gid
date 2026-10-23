import cv2 as cv
import numpy as np

src = cv.imread("test.png")

if src is None:
    print("HATA: test.png dosyasi bulunamadi!")
    exit()

cv.imshow("Orijinal Goruntu", src)
h, w = src.shape[:2]

dst = cv.edgePreservingFilter(src, flags=1, sigma_s=50, sigma_r=0.4)

result = np.zeros((h, w * 2, 3), dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w:w * 2, :] = dst

result = cv.resize(result, (w, h // 2))
cv.imshow("Orijinal ve Filtrelenmis", result)

cv.waitKey(0)
cv.destroyAllWindows()