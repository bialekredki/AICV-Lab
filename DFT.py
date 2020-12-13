import cv2
import numpy
from matplotlib import pyplot
from quantize import quantize


image = cv2.imread('gfx/lena.jpg',0)
q_image = quantize(image,16)
img_float32 = numpy.float32(q_image)

dft = cv2.dft(img_float32, flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = numpy.fft.fftshift(dft)

magnitude_spectrum = 20*numpy.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
inv_dft = numpy.fft.ifftshift(dft_shift)
inv_dft = cv2.idft(inv_dft)
inv_dft = cv2.magnitude(inv_dft[:,:,0],inv_dft[:,:,1])
min,max = numpy.amin(q_image), numpy.amax(q_image)
img_back = cv2.normalize(inv_dft, None, alpha=min, beta=max, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

cv2.imshow('Image', image)
cv2.imshow('Inverted DFT', img_back)

pyplot.imshow(magnitude_spectrum,cmap='gray')
pyplot.show()
pyplot.hist(q_image.ravel(),256,[0,256])
pyplot.hist(img_back.ravel(),256,[0,256])
cv2.imwrite('dft.jpg',numpy.hstack((image,img_back)))
pyplot.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
exit()
