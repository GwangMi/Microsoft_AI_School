import cv2 as cv
import sys

img = cv.imread('Ch.02/soccer.jpg')


if img is None:
    sys.exit('File Not Found')

# Small_image = cv.resize(img, dsize=(0,0), fx=0.3, fy=0.3)
Small_image = cv.resize(img, dsize=(400,300))


cv.imshow('Image Display', Small_image)


cv.imwrite('Ch.02\soccer.jpg', img)

cv.waitKey()

cv.destroyWindow()


import cv2 as cv
import sys
