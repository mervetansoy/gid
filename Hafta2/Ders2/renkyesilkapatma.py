import cv2 as cv

src = cv.imread("res.jpg")
cv.imshow("Orijinal Goruntu", src)

mv = cv.split(src)

mv[1][:, :] = 0
dst1 = cv.merge(mv)
cv.imshow("Yesil Kanal Kapatildi", dst1)

cv.waitKey(0)
cv.destroyAllWindows()