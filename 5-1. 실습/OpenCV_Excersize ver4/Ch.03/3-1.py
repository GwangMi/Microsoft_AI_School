import cv2 as cv
import numpy as np

img = cv.imread('Ch.03\RGB.jpg')
if img is None:
    raise FileNotFoundError("이미지 파일을 찾을 수 없음.")

cv.imshow('Original Image', img)
cv.imshow('Blue Channel', img[:,:,0])
cv.imshow('Green Channel', img[:,:,1])
cv.imshow('Red Channel', img[:,:,2])

cv.waitKey(0)
cv.destroyAllWindows()

