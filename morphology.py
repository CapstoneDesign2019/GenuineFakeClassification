import numpy as np
import cv2

#------------------------
def eroded():
    img = cv2.imread('5.jpg', cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((3,3), np.uint8)

    erosion = cv2.erode(img, kernel, iterations = 1)

    cv2.imwrite('test_erosion.png', erosion)

def denoising():
    img1 = cv2.imread('test_erosion.png', cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((5,5), np.uint8)

    opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel)

    cv2.imwrite('opening.png', opening)
    cv2.imwrite('closing.png', closing)

def morphEx():
    img2 = cv2.imread('test_erosion.png', cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((3,3), np.uint8)

    grad = cv2.morphologyEx(img2, cv2.MORPH_GRADIENT, kernel)
    tophat = cv2.morphologyEx(img2, cv2.MORPH_TOPHAT, kernel)
    blackhat = cv2.morphologyEx(img2, cv2.MORPH_BLACKHAT, kernel)

    cv2.imwrite('grad.png', grad)
    cv2.imwrite('tophat.png', tophat)
    cv2.imwrite('blackhat.png', blackhat)

eroded()
denoising()
morphEx()
