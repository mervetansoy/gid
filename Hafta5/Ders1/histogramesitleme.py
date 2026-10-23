import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def custom_hist(gray):
    h, w = gray.shape
    hist = np.zeros([256], dtype=np.int32)
    for row in range(h):
        for col in range(w):
            pv = gray[row, col]
            hist[pv] += 1
    x_pos = np.arange(0, 256, 1, dtype=np.int32)
    plt.bar(x_pos, hist, align="center", color="red", alpha=0.5)
    plt.xlabel("Piksel Degeri")
    plt.ylabel("Frekans")
    plt.title("Histogram")
    plt.xlim([0, 256])
    plt.show()

src = cv.imread("labirent.jpg")
if src is None:
    print("HATA: labirent.jpg dosyasi bulunamadi!")
    exit()

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow("Orijinal Gri Goruntu", gray)

custom_hist(gray)

dst = cv.equalizeHist(gray)
cv.imshow("Histogram Esitlenmis Goruntu", dst)

custom_hist(dst)

cv.waitKey(0)
cv.destroyAllWindows()