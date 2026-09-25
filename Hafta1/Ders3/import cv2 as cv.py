import cv2 as cv

img = cv.imread("images.png")

cv.namedWindow("Renkli", cv.WINDOW_AUTOSIZE)
cv.imshow("Renkli", img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.namedWindow("Gri Goruntu", cv.WINDOW_AUTOSIZE)
cv.imshow("Gri Goruntu",gray)

cv.imwrite("gray_images.png",gray)
cv.waitKey(0)
cv.destroyAllWindows