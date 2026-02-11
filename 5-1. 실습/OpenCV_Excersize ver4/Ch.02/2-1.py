import cv2 as cv
import sys

img = cv.imread('Ch.02/soccer.jpg', cv.IMREAD_GRAYSCALE)


if img is None:
    sys.exit('File Not Found')

cv.imshow('Image Display', img)

cv.imwrite('Ch.02\soccer.jpg', img)

cv.waitKey()

cv.destroyWindow()


import cv2 as cv
import sys
