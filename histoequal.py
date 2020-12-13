import numpy
import cv2
from quantize import quantize
from matplotlib import pyplot

image = cv2.imread("gfx/dune.jpg",0)
assert(image is not None), "Wrong path to the image"
quant_image = quantize(image,32)
heq_image = cv2.equalizeHist(quant_image)

pyplot.hist(image.ravel(),256,[0,256])
pyplot.hist(heq_image.ravel(),256,[0,256])
pyplot.hist(quant_image.ravel(),256,[0,256])
pyplot.show()
cv2.imshow('origin', image)
cv2.imshow('quantized', quant_image)
cv2.imshow('equalized histogram', heq_image)

res = numpy.hstack((quant_image,heq_image))
cv2.imwrite('heqlf32.jpg',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
exit()