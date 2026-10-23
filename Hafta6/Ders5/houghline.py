import cv2 as cv
import numpy as np

def canny_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    return edges

src = cv.imread("1.jpg")
if src is None:
    print("Goruntu okunamadi!")
    exit()

cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(1)

binary = canny_demo(src)
cv.imshow("binary", binary)
cv.waitKey(1)

linesP = cv.HoughLinesP(binary, 1, np.pi / 180, threshold=55, minLineLength=50, maxLineGap=10)

if linesP is not None:
    for line in linesP:
        # ravel() boyut ne olursa olsun (1, 4) veya (4,) diziyi tek boyutlu [x1, y1, x2, y2] yapar
        x1, y1, x2, y2 = line.ravel()
        cv.line(src, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 1, cv.LINE_AA)

cv.imshow("hough line demo", src)

cv.waitKey(0)
cv.destroyAllWindows()