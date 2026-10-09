import cv2 as cv

img = cv.imread("res.jpg")
cv.namedWindow("Goruntu", cv.WINDOW_AUTOSIZE)
cv.imshow("Orijinal Goruntu", img)

h, w, ch = img.shape
print("h, w, ch =", h, w, ch)

for row in range(h):
    for col in range(w):
        b, g, r = img[row, col]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        img[row, col] = (b, g, r)

cv.imshow("Negatif Goruntu", img)

cv.waitKey(0)
cv.destroyAllWindows()