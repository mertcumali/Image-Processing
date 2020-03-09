import cv2
import numpy as npy

image=cv2.imread('messi.jpg')



def facedetect(img):
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    #attributes of face is got from xml file
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 3)

    #To obtain face according to parameters of function
    cropped=img

    for (x,y,w,h) in faces:

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)# To specify face on the image

        cropped=img[y:(y+h) , x:(x+w)] # To obtain only face from image 

    return cropped

result=facedetect(image)
cv2.imshow('result',result)

cv2.waitKey(0)
cv2.destroyAllWindows
