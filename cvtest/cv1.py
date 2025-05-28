import cv2

s_img = cv2.imread('cvtest.jpg')
c_img = cv2.GaussianBlur(s_img, (7,7), 0)

cv2.imshow('', s_img)
cv2.imshow('converted', c_img)
cv2.waitKey()
