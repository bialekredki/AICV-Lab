import cv2
import numpy
from matplotlib import pyplot
from quantize import quantize
from marioStr import marioSt

def histStrech(image):
    result = numpy.zeros((image.shape[0],image.shape[1]), dtype='uint8')
    min = numpy.min(image)
    max = numpy.max(image)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            result[x,y] = (image[x,y]-min)/(max-min)*255
    return result



image = cv2.imread("gfx/lena.jpg",0)
assert(image is not None), "Wrong path to the image"
quant_image = quantize(image,32)
hs_image = marioSt(quant_image)

pyplot.hist(image.ravel(),256,[0,256])
pyplot.hist(hs_image.ravel(),256,[0,256])
pyplot.hist(quant_image.ravel(),256,[0,256])
pyplot.show()

cv2.imshow('origin', image)
cv2.imshow('quantized', quant_image)
cv2.imshow('streched histogram', hs_image)

res = numpy.hstack((quant_image,hs_image))
cv2.imwrite("hslf32.jpg",res)
cv2.waitKey(0)
cv2.destroyAllWindows()