import cv2
import numpy


img = cv2.imread('gfx/apple.png',0)
equ = cv2.equalizeHist(img)
res = numpy.hstack((img,equ))
cv2.imwrite('res.png',res)
