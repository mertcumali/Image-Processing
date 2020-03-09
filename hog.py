import matplotlib.pyplot as plt

import cv2
from skimage.feature import hog
from skimage import data, exposure


def show_image(img):
    cv2.imshow('Image',img)
    cv2.waitKey(0)

image = cv2.imread('minion.jpg')
fd, hog_image = hog(image, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, multichannel=True)

cv2.imshow('test',hog_image)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

ax1.axis('off')
ax1.imshow(image, cmap=plt.cm.gray)
ax1.set_title('Input image')

# Rescale histogram for better display
hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0,50))


show_image(hog_image_rescaled)

ax2.axis('off')
ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
ax2.set_title('Histogram of Oriented Gradients')
plt.show()