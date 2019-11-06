import cv2, sys
from matplotlib import pyplot as plt
import numpy as np
import os

#image = cv2.imread('download.jpeg')
def crop(root, fname):
    image = cv2.imread(root+fname)
    #image_gray = cv2.imread('download.jpeg', cv2.IMREAD_GRAYSCALE)

    b,g,r = cv2.split(image)
    image2 = cv2.merge([r,g,b])

    #blur = cv2.GaussianBlur(image_gray, ksize=(5,5), sigmaX=0)
    blur = cv2.GaussianBlur(image, ksize=(7,7), sigmaX=5)
    ret, thresh1 = cv2.threshold(blur, 125, 255, cv2.THRESH_BINARY)

    edged = cv2.Canny(blur, 10, 250)
#    cv2.imwrite('/home/lgc/Desktop/newDataSet/edged/'+fname, edged)
    #cv2.waitKey(0)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    #cv2.imwrite('/home/lgc/Desktop/newDataSet/closed/'+fname, closed)

    contours, _ = cv2.findContours(closed.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    total = 0

    # line drawing
    contours_image = cv2.drawContours(image, contours, -1, (0,255,0), 2)
    cv2.imwrite('contours_image.png', contours_image)

    contours_xy = np.array(contours)
    contours_xy.shape

    # x의 min과 max 찾기
    x_min, x_max = 0,0
    value = list()
    for i in range(len(contours_xy)):
        for j in range(len(contours_xy[i])):
            value.append(contours_xy[i][j][0][0]) #네번째 괄호가 0일때 x의 값
            x_min = min(value)
            x_max = max(value)
    print("xmin: " ,x_min)
    print("xmax: " ,x_max)

    # y의 min과 max 찾기
    y_min, y_max = 0,0
    value = list()
    for i in range(len(contours_xy)):
        for j in range(len(contours_xy[i])):
            value.append(contours_xy[i][j][0][1]) #네번째 괄호가 0일때 x의 값
            y_min = min(value)
            y_max = max(value)
    print("ymin: ",y_min)
    print("ymax: ",y_max)

    # image trim 하기
    x = x_min
    y = y_min
    w = x_max-x_min
    h = y_max-y_min

    img_trim = image[y:y+h, x:x+w]
    cv2.imwrite('/home/lgc/Desktop/newDataSet/cropped/'+fname, img_trim)
#    org_image = cv2.imread('org_trim.png')

#    cv2.imwrite('/home/lgc/Desktop/newDataSet/img/'+fname, org_image)



if __name__=='__main__':
    for root, dirs, files in os.walk('/home/lgc/Desktop/newDataSet/trim/'):
        #print(root)
        for fname in files:
        #    print(fname)
            crop(root, fname)
