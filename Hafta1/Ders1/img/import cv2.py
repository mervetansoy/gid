import cv2


img = cv2.imread("res.jpg")

cv2.imshow("res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()