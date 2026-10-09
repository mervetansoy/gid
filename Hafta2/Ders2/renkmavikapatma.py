import cv2 as cv

src = cv.imread("res.jpg")
cv.imshow("Orijinal Goruntu", src)

mv = cv.split(src)

mv[0][:, :] = 0
dst1 = cv.merge(mv)
cv.imshow("Mavi Kanal Kapatildi", dst1)

cv.waitKey(0)
cv.destroyAllWindows()