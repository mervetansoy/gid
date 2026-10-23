import cv2 as cv
import numpy as np

def canny_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    return edges

src = cv.imread("images.png")
if src is None:
    print("HATA: images.png dosyasi bulunamadi!")
    exit()

cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

binary = canny_demo(src)
cv.imshow("binary", binary)

lines = cv.HoughLines(binary, 1, np.pi / 180, 150, None, 0, 0)

if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * a))
        pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * a))
        cv.line(src, pt1, pt2, (0, 0, 255), 3, cv.LINE_AA)

cv.imshow("Hough Cizgileri", src)

cv.waitKey(0)
cv.destroyAllWindows()