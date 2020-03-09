import math
import cv2
import numpy as np


image = cv2.imread('min.jpg', 0).astype(np.float32) / 255

kernel = cv2.getGaborKernel((5, 5),7, 20, 7, 0.5, 5, cv2.CV_32F)
kernel /= math.sqrt((kernel * kernel).sum())

filtered = cv2.filter2D(image, -1, kernel)

cv2.imshow('Origi',image)
cv2.imshow('Gabor',filtered)
h, w = kernel.shape[:2]
kernel = cv2.resize(kernel, (10*w, 10*h), interpolation=cv2.INTER_CUBIC)
cv2.imshow('gabor kernel (resized)', kernel)

cv2.waitKey(0)
cv2.destroyAllWindows

#1.ksize-fotografın bulanıklıgını ayarlar artarsa bulanıklık artar
#2.sigma-gauss genisliğini ayarlar
#3.teta-tespit edilecek ayrıtların yönünü belirler 0 iken x ekseinine dik ayrtıları belriler
# (arttıkca resimde arkaplanı geride bırakarak cisimler ve ayrıtları ortaya cıkar 20,100,1500 )
#4.lambda-dalga boyu ile ilgili değiştikce ayrıtların cizgi sayısı degisiyor(teta 0iken lambda=2,5,7 dene)
#5.gama-gamanın değeri arttıkca orjinal resme tıpatıp benzemeye baslıyor(1-10-100-1000 dene)
#6.psi-faz açısı-parlaklıgı ayarlar kimi durumlarda pikselleri bile yok edecek duruma gelir(lambda 2 psi 90)
