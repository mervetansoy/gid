import numpy as np
import cv2 as cv

def process(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    corners = cv.goodFeaturesToTrack(gray, maxCorners=35, qualityLevel=0.05, minDistance=10)
    if corners is None:
        return image
    for pt in corners:
        print(pt)
        b = np.random.randint(0, 256)
        g = np.random.randint(0, 256)
        r = np.random.randint(0, 256)
        x = np.int32(pt[0][0])
        y = np.int32(pt[0][1])
        cv.circle(image, (int(x), int(y)), 5, (int(b), int(g), int(r)), 2)
    return image

src = cv.imread("img.jpg")
if src is None:
    raise FileNotFoundError("img.jpg dosyasi bulunamadi!")
original = src.copy()
result = process(src)

cv.imshow("Orijinal Goruntu", original)
cv.imshow("Shi-Tomasi Kose Saptama", result)
cv.waitKey(0)
cv.destroyAllWindows()