import cv2 as cv
import sys

img = cv.imread('Ch.02/soccer.jpg')


if img is None:
    sys.exit('File Not Found')

Gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


cv.imshow('Image Display', Gray_image)


cv.imwrite('Ch.02\soccer.jpg', img)

cv.waitKey()

cv.destroyWindow()


import cv2 as cv
import sys
