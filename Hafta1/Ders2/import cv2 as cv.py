import cv2 as cv

src=cv.imread("images.jpg")

cv.namedWindow("giris", cv.WINDOW_AUTOSIZE)
cv.imshow("giris",src)

dst = cv.applyColorMap(src, cv.COLORMAP_PINK)
cv.namedWindow("Sonuc", cv.WINDOW_AUTOSIZE)
cv.imshow("Sonuc",dst)
cv.waitKey(0)
cv.destroyAllWindows