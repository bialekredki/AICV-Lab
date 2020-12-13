import numpy
import cv2
from quantize import  quantize
from matplotlib import pyplot

def negative(image:numpy.array):
    result = numpy.zeros((image.shape[0], image.shape[1]), dtype='uint8')
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            result[x,y] = 255-image[x,y]
    return result


image = cv2.imread("gfx/lena.jpg",0)
assert (image is not None), "Wrong image's path"
quant_image = quantize(image,8)
neg_image = negative(quant_image)
cv2.imshow("Image", image)
cv2.imshow("Quantized", quant_image)
cv2.imshow("Negative", neg_image)
pyplot.hist(quant_image.ravel(), 256, [0,256])
pyplot.hist(neg_image.ravel(), 256, [0,256])
cv2.imwrite('neg.jpg',numpy.hstack((quant_image,neg_image)))
pyplot.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
exit()