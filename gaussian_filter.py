import numpy as np
import cv2

#Gaussian Filter 5x5 kernel
img=cv2.imread('tom.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernell=[[1,4,6,4,1],
        [4,16,24,16,4],
        [6,24,36,24,6],
        [4,16,24,16,4],
        [1,4,6,4,1]]

height=len(gray)
weight=len(gray[0])

sum_kernell=0
for i in range(len(kernell)):
    for j in  range(len(kernell[0])):
        sum_kernell+=kernell[i][j]    
        

copy=gray.copy()


for y in range(2,height-2):
    for x in range(2,weight-2):
        all_sum=0
        for i in range(-2,3):  
            for j in range(-2,3):
                p=gray[y+i][x+j]
                g=kernell[2+i][2+j]
                all_sum+=p*g/sum_kernell
        copy[y][x]=all_sum

cv2.imshow('Original image',img)

cv2.imshow('Gray image', gray)
cv2.imwrite('GaussianFilter.jpg',copy)

cv2.imshow('Copy',copy)
 
cv2.waitKey(0)
cv2.destroyAllWindows



