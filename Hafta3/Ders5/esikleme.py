import cv2 as cv

src = cv.imread("res.jpg")
T = 127

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow("Orijinal Goruntu", src)
cv.imshow("Gri Goruntu", gray)

for i in range(5):
    ret, binary = cv.threshold(gray, T, 255, i)
    cv.imshow("Binary " + str(i), binary)

cv.waitKey(0)
cv.destroyAllWindows()