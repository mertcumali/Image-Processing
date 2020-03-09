import cv2
import numpy as np

#Median Filter
img=cv2.imread('adam.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height = img.shape[0]
width = img.shape[1]

copy=gray.copy()


for y in range(3,height-3):
    for x in range(3,width-3):
        arr=[]
        for i in range(-3,4):
            for j in range(-3,4):
                pixel=gray.item(y+i,x+j)
                arr.append(pixel) 
        arr.sort()
        median = arr[24]       
        copy.itemset((y,x), median)

                
cv2.imshow('Original image',img)

cv2.imshow('Gray image', gray)

cv2.imshow('Median Filter',copy)
cv2.imwrite('median.jpg',copy)

cv2.waitKey(0)
cv2.destroyAllWindows

