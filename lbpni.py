import cv2
import numpy as npy

#lbp best version
img=cv2.imread('min.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image',img)

cv2.imshow('Gray image', gray)

 
cv2.waitKey(0)
cv2.destroyAllWindows

def change(sayi,arr):
    sum=0
    size=len(arr) #verilerin sayısı
    for x in range(len(arr)):
        sum+=arr[x]
    ort=sum/size #ortalama buldum

    for j in range(len(arr)):
        if(arr[j]>=ort):
            arr[j]=1
        else: 
            arr[j]=0
            
    total=0        
    for y in range(len(arr)):
        total+=arr[y]*2**(y)
     
    return total

copy=gray.copy()


for y in range(2,len(gray)-2):
    for x in range(2,len(gray[0])-2):
        arr=[gray[y][x+2],gray[y+2][x+2],gray[y+2][x],
        gray[y+2][x-2],gray[y][x-2],gray[y-2][x-2],
        gray[y-2][x],gray[y-2][x+2]]               
        copy[y][x]=change(gray[y][x],arr)
                


cv2.imshow('Filter',copy)
cv2.imwrite('savedNI.jpg',copy)
cv2.waitKey(0)
cv2.destroyAllWindows
