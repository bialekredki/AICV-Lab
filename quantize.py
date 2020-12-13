import numpy
def quantize(image,level=8):
    result = numpy.zeros((image.shape[0], image.shape[1]), dtype='uint8')
    min = numpy.min(image)
    max = numpy.max(image)
    step = (max-min)//level
    counter = 0
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            result[x,y]=image[x,y]
            while True:
                if result[x,y] <= min+step or counter >= level:
                    break
                else:
                    result[x,y] = result[x,y] - step
                    counter += 1
            result[x,y] = counter*step+min+step//2
            counter=0
    return result