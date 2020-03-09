import cv2
import numpy as npy

#Maximum Filter

img=cv2.imread('noise.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image',img)

cv2.imshow('Gray image', gray)

 
cv2.waitKey(0)
cv2.destroyAllWindows

     

def change(sayi,arr):
    max=0
    for x in range(len(arr)):
        if(arr[x]>max):
            max=arr[x]
    return max

copy=gray.copy()


for y in range(1,len(gray)-1):
        for x in range(1,len(gray[0])-1):
                arr=[gray[y-1][x-1],gray[y-1][x],gray[y-1][x+1],
                gray[y][x+1],gray[y+1][x+1],gray[y+1][x],
                gray[y+1][x-1],gray[y][x-1]]               
                copy[y][x]=change(gray[y][x],arr)
                


cv2.imshow('Max Filter',copy)
#cv2.imwrite('max.jpg',copy)

cv2.waitKey(0)
cv2.destroyAllWindows








