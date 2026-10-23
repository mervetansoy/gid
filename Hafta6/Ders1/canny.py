import cv2 as cv

src = cv.imread("images.jpg")
if src is None:
    print("Goruntu bulunamadi!")
    exit()

print("Goruntu boyutu:", src.shape)
cv.imshow("Orijinal Goruntu", src)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow("Gri Goruntu", gray)

blur = cv.GaussianBlur(gray, (5, 5), 0)
cv.imshow("Gaussian", blur)

edge = cv.Canny(blur, 50, 150)
cv.imshow("Canny", edge)

edge1 = cv.Canny(blur, 30, 100)
edge2 = cv.Canny(blur, 50, 150)
edge3 = cv.Canny(blur, 100, 200)

cv.imshow("Canny 30-100", edge1)
cv.imshow("Canny 50-150", edge2)
cv.imshow("Canny 100-200", edge3)

cv.waitKey(0)
cv.destroyAllWindows()