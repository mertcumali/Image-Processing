import math
import cv2
import numpy as np


image = cv2.imread('tom.jpg', 0).astype(np.float32) / 255

kernel = cv2.getGaborKernel((5, 5),7, 20, 7, 0.5, 5, cv2.CV_32F)
kernel /= math.sqrt((kernel * kernel).sum())

filtered = cv2.filter2D(image, -1, kernel)

cv2.imshow('Original',image)
cv2.imshow('Gabor',filtered)
h, w = kernel.shape[:2]
kernel = cv2.resize(kernel, (10*w, 10*h), interpolation=cv2.INTER_CUBIC)
cv2.imshow('gabor kernel (resized)', kernel)

cv2.waitKey(0)
cv2.destroyAllWindows

