import cv2 as cv
import numpy as np

src1 = cv.imread("elma1.jpg")
src2 = cv.imread("elma2.jpg")

src2=cv.resize(src2,(src1.shape[1],src1.shape[0]))

h,w,ch=src1.shape
print("Yükseklik:", h, "Genislik:",w,"Kanal:",ch)

div_result=np.zeros(src1.shape,src1.dtype)
cv.divide(src1,src2,div_result)

cv.imshow("elma1",src1)
cv.imshow("elma2",src2)
cv.imshow("Bolme Sonucu",div_result)

cv.waitKey(0)
cv.destroyAllWindows
