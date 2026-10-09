import cv2 as cv
import numpy as np

src = cv.imread("res.jpg")

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
print("Goruntu boyutu: ", gray.shape)
print(gray)

gray = np.float32(gray)
print(gray)

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(gray)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))

means, stddev = cv.meanStdDev(gray)
print("mean: %.2f, stddev: %.2f" % (means[0][0], stddev[0][0]))

dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=0, beta=1.0, norm_type=cv.NORM_MINMAX)
print(dst)

cv.imshow("Normalize", dst)

cv.waitKey(0)
cv.destroyAllWindows()