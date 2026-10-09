import cv2 as cv
import numpy as np

src = cv.imread("res.jpg", cv.IMREAD_GRAYSCALE)

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(src)
print("Minimum değer:", min_value)
print("Maksimum değer:", max_value)
print("Minimum konum:", min_loc)
print("Maksimum konum:", max_loc)
mean, stddev = cv.meanStdDev(src)
print("Ortalama:", mean[0][0])
print("Standart sapma:", stddev[0][0])