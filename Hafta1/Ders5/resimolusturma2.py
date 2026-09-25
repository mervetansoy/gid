import cv2 as cv
import numpy as np

img = np.ones((550, 770, 3), dtype=np.uint8) * 255

black = (0, 0, 0)
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)

cv.rectangle(img, (480, 250), (100, 450), black, 8)
cv.rectangle(img, (580, 150), (200, 350), black, 8)

cv.line(img, (100, 450), (200, 350), black, 8)
cv.line(img, (480, 250), (580, 150), black, 8)
cv.line(img, (100, 250), (200, 150), black, 8)
cv.line(img, (480, 450), (580, 350), black, 8)

start_point = (100,500)
font_thickness = 2
font_size = 1
font = cv.FONT_HERSHEY_DUPLEX
cv.putText(img, "Goruntu Isleme Teknikleri", start_point, font, font_size, black, font_thickness)

cv.namedWindow("Olusturulan Resim", cv.WINDOW_AUTOSIZE)
cv.imshow("Olusturulan Resim", img)
cv.waitKey(0)
cv.destroyAllWindows()