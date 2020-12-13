import numpy
import cv2
import copy

def gaussianNoise(image,mean:float = 0.0, var:float = 1.0):
    row, col= image.shape
    noise = numpy.random.normal(mean, var**0.5, (row, col))
    noise = noise.reshape(row, col)
    return (noise+image).astype("uint8")

def spNoise(image, spratio:float = 0.5, amount:float=0.10):
    row, col = image.shape
    result = copy.deepcopy(image)
    XY_CACHE = []
    salt = int(image.size*amount*(1.0 - spratio))
    pepper = int(-image.size*amount*(spratio - 1.0))
    while salt > 0 :
            x = numpy.random.randint(0,row)
            y = numpy.random.randint(0,col)
            if not (x,y) in XY_CACHE:
                result[x,y] = 255
                XY_CACHE.append((x,y))
                salt = salt - 1
    while pepper > 0 :
            x = numpy.random.randint(0,row)
            y = numpy.random.randint(0,col)
            if not (x,y) in XY_CACHE:
                result[x,y] = 0
                XY_CACHE.append((x,y))
                pepper = pepper - 1

    return result



