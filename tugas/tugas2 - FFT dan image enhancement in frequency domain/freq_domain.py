# source: https://medium.com/@devangdayal/frequency-domain-filtering-on-an-image-using-opencv-26bfcc97e23b

import numpy as np
import pandas as pd
import cv2

# img_root="Images/"
# img_name="testImage.jpg"

# Reading the Image
img = cv2.imread("demofadhil.jpg",cv2.IMREAD_UNCHANGED)

domainFilter = cv2.edgePreservingFilter(img, flags=1, sigma_s=60, sigma_r=0.6)
cv2.imshow('Domain Filter',domainFilter)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Let us try to Smoothen this image using the Gaussian Blur Method from OpenCV Library. 
# Gaussian blur (also known as Gaussian smoothing) is the result of blurring an image by a Gaussian function.
gaussBlur = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow("Gaussian Smoothing",np.hstack((img,gaussBlur)))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Let us try to perform Mean Filtering Techniques on this image.
# The idea of mean filtering is simply to replace each pixel value in an image with the mean (`average’) value of its neighbours,
# including itself. This has the effect of eliminating pixel values that are unrepresentative of their surroundings. 
# Mean filtering is usually thought of as a convolution filter. Like other convolutions, it is based around a kernel, which represents the shape and size of the neighbourhood to be sampled when calculating the mean.
kernel = np.ones((10,10),np.float32)/25
meanFilter = cv2.filter2D(img,-1,kernel)
cv2.imshow("Mean Filtered Image",np.hstack((img, meanFilter)))
cv2.waitKey(0)
cv2.destroyAllWindows()


# Median Filter
# Median filtering is a nonlinear process useful in reducing impulsive, or salt-and-pepper noise
medianFilter = cv2.medianBlur(img,5)
cv2.imshow("Median Filter",np.hstack((img, medianFilter)))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Bilateral filter
# A Bilateral filter is a non-linear, edge-preserving, and noise-reducing smoothing filter for images.
# It replaces the intensity of each pixel with a weighted average of intensity values from nearby pixels.
# This weight can be based on a Gaussian distribution.
print("Bilateral Filter")
bilFil = cv2.bilateralFilter(img, 60, 60, 60)
cv2.imshow("Bilateral Filter",np.hstack((img, bilFil)))
cv2.waitKey(0)
cv2.destroyAllWindows()


# For High Band Pass Filter
highPass = img - gaussBlur
# or We can use this statement to filter the high pass image
#highPass = highPass + 127*np.ones(img.shape, np.uint8)
cv2.imshow("High Pass",np.hstack((img, highPass)))
cv2.waitKey(0)
cv2.destroyAllWindows()

# For Low Band Pass Filter
lowPass = cv2.filter2D(img,-1, kernel)
lowPass = img - lowPass
cv2.imshow("Low Pass",np.hstack((img, lowPass)))
cv2.waitKey(0)
cv2.destroyAllWindows()