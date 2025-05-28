import cv2

s1 = cv2.imread('c1.jpg')
s2 = cv2.imread('c2.jpg')

diff = cv2.absdiff(s1, s2)
gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

r,thre = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
cann = cv2.Canny(diff,100,200)

contours, r1 = cv2.findContours(thre, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(s1, contours, -1, (0, 255, 0), 2)

cv2.imshow("diff", diff)
cv2.imshow("thre", thre)
cv2.imshow("canny", cann)
cv2.imshow("contours", s1)

cv2.waitKey(0)
cv2.destroyAllWindows()
