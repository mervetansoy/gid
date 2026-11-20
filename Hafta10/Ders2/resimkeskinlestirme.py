import cv2 as cv
import numpy as np

src = cv.imread("res.jpg")
if src is None:
    raise FileNotFoundError("res.jpg dosyasi bulunamadi!")

sharpen_op = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
sharpen_image = cv.filter2D(src, cv.CV_32F, sharpen_op)
sharpen_image = cv.convertScaleAbs(sharpen_image)

cv.imshow("Orijinal Goruntu", src)
cv.imshow("Keskinlestirilmis Goruntu", sharpen_image)
cv.waitKey(0)
cv.destroyAllWindows()