import cv2 as cv

src1 = cv.imread("miuul.png")
src2 = cv.imread("opencv.png")
src3 = cv.imread("labirent.jpg")

if src1 is None or src2 is None or src3 is None:
    print("HATA: Resim dosyalarindan biri bulunamadi!")
    exit()

cv.imshow("Resim 1 - Miuul", src1)
cv.imshow("Resim 2 - OpenCV", src2)
cv.imshow("Resim 3 - Labirent", src3)

hsv1 = cv.cvtColor(src1, cv.COLOR_BGR2HSV)
hsv2 = cv.cvtColor(src2, cv.COLOR_BGR2HSV)
hsv3 = cv.cvtColor(src3, cv.COLOR_BGR2HSV)

hist1 = cv.calcHist([hsv1], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist2 = cv.calcHist([hsv2], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist3 = cv.calcHist([hsv3], [0, 1], None, [60, 64], [0, 180, 0, 256])

cv.normalize(hist1, hist1, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist2, hist2, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist3, hist3, 0, 1.0, cv.NORM_MINMAX)

sonuc12 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
sonuc13 = cv.compareHist(hist1, hist3, cv.HISTCMP_CORREL)
sonuc23 = cv.compareHist(hist2, hist3, cv.HISTCMP_CORREL)

print("Miuul - OpenCV benzerligi  :", sonuc12)
print("Miuul - Labirent benzerligi:", sonuc13)
print("OpenCV - Labirent benzerligi:", sonuc23)

cv.waitKey(0)
cv.destroyAllWindows()