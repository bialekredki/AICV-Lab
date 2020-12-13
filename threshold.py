import cv2
import numpy
from matplotlib import pyplot

lena = cv2.imread('gfx/lena.jpg',0)
assert (lena is not None), "Wrong path to the image"
ret,binary_lena = cv2.threshold(lena,127,255, cv2.THRESH_BINARY)
ret,threshold_lena = cv2.threshold(lena,127,255, cv2.THRESH_TOZERO)

cv2.imshow('Binary thresholding',binary_lena)
cv2.imshow('To zero thresholding',threshold_lena)
pyplot.hist(binary_lena.ravel(), 256, [0,256])
pyplot.hist(threshold_lena.ravel(), 256, [0,256])
pyplot.show()
cv2.imwrite("thresh.jpg", numpy.hstack((binary_lena,threshold_lena)))
cv2.waitKey(0)
cv2.destroyAllWindows()
exit()