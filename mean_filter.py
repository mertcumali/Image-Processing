import cv2
import numpy as npy

#Mean Filter(Box Filter) with small kernel

img=cv2.imread('adam.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image',img)

cv2.imshow('Gray image', gray)

 
cv2.waitKey(0)
cv2.destroyAllWindows

     

def change(num,arr):
        total=0        
        for y in range(len(arr)):
            total+=arr[y]
        total+=num
        total=total/9
        result=round(total)
        return result

copy=gray.copy()


for y in range(1,len(gray)-1):
        for x in range(1,len(gray[0])-1):
                arr=[gray[y-1][x-1],gray[y-1][x],gray[y-1][x+1],
                gray[y][x+1],gray[y+1][x+1],gray[y+1][x],
                gray[y+1][x-1],gray[y][x-1]]               
                copy[y][x]=change(gray[y][x],arr)
                


cv2.imshow('Mean Filter',copy)
cv2.imwrite('Mean.jpg',copy)

cv2.waitKey(0)
cv2.destroyAllWindows








