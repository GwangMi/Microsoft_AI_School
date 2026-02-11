import cv2 as cv
import numpy as np

img = cv.imread('Ch.03\dog.jpg', cv.IMREAD_GRAYSCALE)

ret, binary_img = cv.threshold(img, 0, 255,
                               cv.THRESH_BINARY + cv.THRESH_OTSU)

print("자동 계산된 임계값:", ret)


cv.imshow('Original', img)
cv.imshow('Otsu Thresholding', binary_img)
cv.waitKey(0)
cv.destroyAllWindows()

