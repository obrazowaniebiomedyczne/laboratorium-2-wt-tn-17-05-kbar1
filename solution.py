import cv2 as cv
import numpy as np
from skimage import util, io, filters, morphology, data

# Zadanie na ocenę dostateczną
def renew_pictures():
    kernel = np.ones((2,2),np.uint8)
    img = cv.imread('figures/crushed.png',0)
    erosion = cv.erode(img,kernel,iterations = 1)
    cv.imwrite("results/crushed.png", erosion)
    kernel2 = np.ones((2,2),np.uint8)
    img2 = cv.imread('figures/crushed2.png',0)
    erosion2 = cv.erode(img2,kernel2,iterations = 1)
    dilation = cv.dilate(erosion2,kernel,iterations = 2)
    cv.imwrite("results/crushed2.png", dilation)
    kernel3 = np.ones((4,3),np.uint8)
    img3 = cv.imread('figures/crushed3.png',0)
    dilation2 = cv.dilate(img3,kernel3,iterations = 1)
    erosion3 = cv.erode(dilation2,kernel3,iterations = 2)
    opening = cv.morphologyEx(erosion3, cv.MORPH_OPEN, kernel3)
    cv.imwrite("results/crushed3.png", opening)
    kernel4 = np.ones((4,3),np.uint8)
    img4 = cv.imread('figures/crushed4.png',0)
    dilation2 = cv.dilate(img4,kernel4,iterations = 1)
    erosion3 = cv.erode(dilation2,kernel4,iterations = 2)
    opening = cv.morphologyEx(erosion3, cv.MORPH_OPEN, kernel4, iterations = 1)
    cv.imwrite("results/crushed4.png", opening)

    pass


# Zadanie na ocenę dobrą
def own_simple_erosion(image):
    new_image = np.zeros(image.shape, dtype=image.dtype)

    # ---------------
    # Do uzupełnienia
    # ---------------

    return new_image


# Zadanie na ocenę bardzo dobrą
def own_erosion(image, kernel=None):
    new_image = np.zeros(image.shape, dtype=image.dtype)
    if kernel is None:
        kernel = np.array([[0, 1, 0],
                           [1, 1, 1],
                           [0, 1, 0]])

    # ---------------
    # Do uzupełnienia
    # ---------------

    return new_image
