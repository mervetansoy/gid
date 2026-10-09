import cv2 as cv

img = cv.imread("elma1.jpg")
cv.namedWindow("RGB", cv.WINDOW_AUTOSIZE)
cv.imshow("RGB", img)
cv.waitKey(1)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GRAY", gray)
cv.waitKey(1)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)
cv.waitKey(1)

cv.waitKey(0)
cv.destroyAllWindows()
