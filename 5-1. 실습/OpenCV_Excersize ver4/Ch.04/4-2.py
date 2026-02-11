import cv2 as cv
import numpy as np

img = cv.imread('Ch.04\soccer.jpg', cv.IMREAD_GRAYSCALE)

blurred = cv.GaussianBlur(img, (5,5), 1.4)

edges = cv.Canny(blurred, 100, 200)

cv.imshow('Original', img)
cv.imshow('Canny Edge', edges)

cv.waitKey(0)
cv.destroyAllWindows()



