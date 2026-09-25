import cv2 as cv
import numpy as np

src1 = cv.imread("elma1.jpg")
src2 = cv.imread("elma2.jpg")

src2=cv.resize(src2,(src1.shape[1],src1.shape[0]))

h,w,ch=src1.shape
print("Yükseklik:", h, "Genislik:",w,"Kanal:",ch)

mul_result=np.zeros(src1.shape,src1.dtype)
cv.multiply(src1,src2,mul_result)

cv.imshow("elma1",src1)
cv.imshow("elma2",src2)
cv.imshow("Carpma Sonucu",mul_result)

cv.waitKey(0)
cv.destroyAllWindows
