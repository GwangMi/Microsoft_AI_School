import cv2 as cv
import numpy as np

img = cv.imread('Ch.04\soccer.jpg', cv.IMREAD_GRAYSCALE)

sobel_x = cv.Sobel(img, cv.CV_64F, 1,0, ksize=3)
sobel_y = cv.Sobel(img, cv.CV_64F, 0,1, ksize=3)


magnitude = np.sqrt(sobel_x ** 2 + sobel_y **2)

abs_sobel_x = cv.convertScaleAbs(sobel_x)
abs_sobel_y = cv.convertScaleAbs(sobel_y)
edge_strength =  cv.convertScaleAbs(magnitude)

cv.imshow('Original', img)
cv.imshow('Sobel_x', abs_sobel_x)
cv.imshow('Sobel_y', abs_sobel_y)
cv.imshow('Edge_strength(Magnitude)', edge_strength)

cv.waitKey(0)
cv.destroyAllWindows()




