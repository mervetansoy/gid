import cv2 as cv

img = cv.imread("res.jpg")
cv.namedWindow("Goruntu", cv.WINDOW_AUTOSIZE)
cv.imshow("Goruntu", img)

h, w, ch = img.shape
print("h, w, ch =", h, w, ch)

cv.waitKey(0)
cv.destroyAllWindows()