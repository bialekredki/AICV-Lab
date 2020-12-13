import cv2
import numpy
import noise

def menu():
    while(True):
        print("1. Task 1 || Gaussian noise\n2. Task 2 || S&P noise"
              "\n3. Task 3 || Sobel filter\n"
              "4. Task 4 || Sobel filter and Gaussian noise\n"
              "5. Task 5 || Laplace filter\n"
              "6. Exit")
        option = int(input())
        if option > 0 and option < 7:
            return option

def sharpen(img):
    kernel = numpy.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    return cv2.filter2D(img,-1,kernel)

def showImages(imgs:tuple):
    for i in range(len(imgs)):
        cv2.imshow("Image {}".format(i), imgs[i])
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task1():
    gn1 = noise.gaussianNoise(image)
    gn2 = noise.gaussianNoise(image,-10,20)
    gn1f = cv2.blur(gn1,(3,3))
    gn2f = cv2.blur(gn2,(3,3))
    gn1f = sharpen(gn1f)
    gn2f = sharpen(gn2f)
    showImages((gn1f,gn2f,image))

def task2():
    sp1 = noise.spNoise(image)
    sp2 = noise.spNoise(image)
    sp1f = sharpen(cv2.medianBlur(sp1,5))
    sp2f = sharpen(cv2.medianBlur(sp2,5))
    showImages((sp1f,sp2f,image))

def task3():
    sbx = cv2.Sobel(image,cv2.CV_64F, 1 , 0 , ksize=5)
    sby = cv2.Sobel(image,cv2.CV_64F, 0 , 1 , ksize=5)
    sbxy = cv2.Sobel(image,cv2.CV_64F, 1 , 1 , ksize=5)
    showImages((sbx,sby,sbxy))

def task4():
    gn = noise.gaussianNoise(image,100,200)
    sbxy = cv2.Sobel(image,cv2.CV_64F, 1 , 1 , ksize=5)
    showImages((gn,sbxy))

def task5():
    kernel = numpy.array([[-1, -1, -1],
                          [-1, 8, -1],
                          [-1, -1, -1]])
    lplc = cv2.filter2D(image,-1,kernel)
    showImages((image,lplc))

image = cv2.imread("gfx/lena.jpg", 0)
assert (image is not None), "Wrong path to the image"

while(True):
    m = menu()
    if m == 1:
        task1()
    elif m == 6:
        exit()
    elif m == 2:
        task2()
    elif m == 3:
        task3()
    elif m == 4:
        task4()
    elif m == 5:
        task5()