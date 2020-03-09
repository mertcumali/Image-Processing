import cv2
import numpy as npy
#Minimum Filter

img=cv2.imread('adam.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image',img)

cv2.imshow('Gray image', gray)

 
cv2.waitKey(0)
cv2.destroyAllWindows

     

def change(arr):
    min=255
    for x in range(len(arr)):
        if(arr[x]<min):
            min=arr[x]
    return min

copy=gray.copy()


for y in range(1,len(gray)-1):
        for x in range(1,len(gray[0])-1):
                arr=[gray[y-1][x-1],gray[y-1][x],gray[y-1][x+1],
                gray[y][x+1],gray[y+1][x+1],gray[y+1][x],
                gray[y+1][x-1],gray[y][x-1]]               
                copy[y][x]=change(gray[y][x],arr)
                


cv2.imshow('Min Filter',copy)


cv2.waitKey(0)
cv2.destroyAllWindows








