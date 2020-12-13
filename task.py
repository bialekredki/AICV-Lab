import cv2
import numpy

scale = 0.2;

original_img = cv2.imread('gfx/flower.jpg')
nnm_img = cv2.resize(original_img, None, fy=scale,fx=scale, interpolation = cv2.INTER_NEAREST)
bil_img = cv2.resize(original_img, None, fy=scale,fx=scale, interpolation = cv2.INTER_LINEAR)
bic_img = cv2.resize(original_img, None, fy=scale,fx=scale, interpolation = cv2.INTER_CUBIC)

cv2.imshow('Original', original_img)
cv2.imshow('Nearest neighbour', nnm_img)
cv2.imshow('Bilinear', bil_img)
cv2.imshow('Bicubic', bic_img)

cv2.waitKey(0)
cv2.destroyAllWindows()