import cv2 as cv

src = cv.imread("images.jpg")
h, w = src.shape[:2]
print("Goruntu boyutu:", w, "x", h)
img = src.copy()

roi = img[80:220, 40:520, :]
print("ROI boyutu:", roi.shape)
cv.imshow("Orijinal Goruntu", src)
cv.imshow("ROI", roi)

res = cv.resize(roi, None, fx=0.4, fy=0.4, interpolation=cv.INTER_AREA)
print("Kucuk ROI boyutu:", res.shape)
cv.imshow("Kucultulmus ROI", res)

rh, rw = res.shape[:2]
img[0:rh, 0:rw, :] = res
cv.imshow("ROI Eklenmis Goruntu", img)

cv.waitKey(0)
cv.destroyAllWindows()
