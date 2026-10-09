import cv2 as cv
import numpy as np

image = np.zeros((512, 512, 3), dtype=np.uint8)

cv.rectangle(image, (100, 100), (300, 300), (255, 0, 0), 2, cv.LINE_8, 0)
cv.circle(image, (256, 256), 50, (0, 0, 255), 2, cv.LINE_8, 0)
cv.ellipse(image, (256, 256), (150, 50), 360, 0, 360, (0, 255, 0), 2, cv.LINE_8, 0)

cv.imshow("Geometrik Sekiller", image)
cv.waitKey(1)

cv.waitKey(0)
cv.destroyAllWindows()