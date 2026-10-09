import cv2 as cv
import numpy as np

src = cv.imread("res.jpg", cv.IMREAD_GRAYSCALE)

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(src)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))
print("min_loc:", min_loc, "max_loc:", max_loc)

means, stddev = cv.meanStdDev(src)
print("means: %.2f, stddev: %.2f" % (means[0][0], stddev[0][0]))