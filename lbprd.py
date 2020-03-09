import cv2
import numpy as npy

#lbp version

img=cv2.imread('min.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image',img)

cv2.imshow('Gray image', gray)

 
cv2.waitKey(0)
cv2.destroyAllWindows

def change(arr_in,arr_out):
    size=len(arr_in)
    result=[None]*size

    for j in range(size):
        if(arr_out[j]>=arr_in[j]):
            result[j]=1
        else: 
            result[j]=0
            
    total=0        
    for y in range(len(result)):
        total+=result[y]*2**y
     
    return total

copy=gray.copy()


for y in range(2,len(gray)-2):
    for x in range(2,len(gray[0])-2):
        arr_out=[gray[y][x+2],gray[y+2][x+2],gray[y+2][x],
        gray[y+2][x-2],gray[y][x-2],gray[y-2][x-2],
        gray[y-2][x],gray[y-2][x+2]]
        arr_in=[gray[y][x+1],gray[y+1][x+1],gray[y+1][x],
        gray[y+1][x-1],gray[y][x-1],gray[y-1][x-1],
        gray[y-1][x],gray[y-1][x+1]]               
        copy[y][x]=change(arr_in,arr_out)
                


cv2.imshow('Filter',copy)
cv2.imwrite('savedRD.jpg',copy)

cv2.waitKey(0)
cv2.destroyAllWindows
