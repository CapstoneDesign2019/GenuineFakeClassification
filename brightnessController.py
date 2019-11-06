import numpy as np
import cv2
import PIL

import os


src = '/home/lgc/Desktop/Dataset'
dst = '/home/lgc/Desktop/realDataset2/'
def whitening():
    for root, dirs, files in os.walk(src):
        for fname in files:
            full_fname = os.path.join(root, fname)
            print(full_fname)
            #cv2.IMREAD_COLOR
            img=cv2.imread(full_fname,cv2.IMREAD_GRAYSCALE)
            fileNameWithoutExt = full_fname.split('/')[-1].split('.')[0]
            imgHeight, imgWidth = img.shape[:2]
            print(imgHeight,imgWidth)
            flag=True #255가 넘어가면 flag down
            number=0
            if not os.path.exists(dst+fileNameWithoutExt):
                os.mkdir(dst+fileNameWithoutExt)
            while flag:
                for i in range(0,imgHeight): #이미지의 세로, 가로 명도 조절
                    for j in range(0,imgWidth):
                    #    print(img[i,j])
                        if(img[i,j]+10<255):
                            img[i,j]+=1
                        # if img[i,j]>120 and img[i,j]<130:
                        #     img[i,j]=0
                        #     #img[i,j]=0
                        # else:
                        #     img[i,j]=255
                        # img[i,j]-=1
                number+=1

                cv2.imwrite(dst+fileNameWithoutExt+'/'+'w'+str(number)+'.png',img)
                if number==200:
                    break

def darkening():
    for root, dirs, files in os.walk(src):
        for fname in files:
            full_fname = os.path.join(root, fname)
            print(full_fname)

            #cv2.IMREAD_COLOR
            img=cv2.imread(full_fname,cv2.IMREAD_GRAYSCALE)
            fileNameWithoutExt = full_fname.split('/')[-1].split('.')[0]
            imgHeight, imgWidth = img.shape[:2]
            print(imgHeight,imgWidth)
            flag=True #255가 넘어가면 flag down
            number=0
            if not os.path.exists(dst+fileNameWithoutExt):
                os.mkdir(dst+fileNameWithoutExt)
            while flag:
                for i in range(0,imgHeight): #이미지의 세로, 가로 명도 조절
                    for j in range(0,imgWidth):
                    #    print(img[i,j])
                        if(img[i,j]-10>0):
                            img[i,j]-=1
                        # if img[i,j]>120 and img[i,j]<130:
                        #     img[i,j]=0
                        #     #img[i,j]=0
                        # else:
                        #     img[i,j]=255
                        # img[i,j]-=1
                number+=1

                cv2.imwrite(dst+fileNameWithoutExt+'/'+'d'+str(number)+'.png',img)
                if number==200:
                    break
if __name__=='__main__':
    whitening()
    darkening()
