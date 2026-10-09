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
    plt.title("Gri Goruntu Histogrami")
    plt.xlim([0, 256])
    plt.show()

def image_hist(image):
    colors = ("blue", "green", "red")
    for i, color in enumerate(colors):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.xlabel("Piksel Degeri")
    plt.ylabel("Frekans")
    plt.title("BGR Renk Kanallari Histogrami")
    plt.show()

src = cv.imread("img.jpg")
if src is None:
    print("HATA: img.jpg dosyasi bulunamadi!")
    exit()

cv.imshow("Orijinal Goruntu", src)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow("Gri Goruntu", gray)

custom_hist(gray)
image_hist(src)

cv.waitKey(0)
cv.destroyAllWindows()
