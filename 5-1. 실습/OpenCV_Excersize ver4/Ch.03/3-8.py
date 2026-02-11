import cv2 as cv
import numpy as np

img = np.zeros((300,300,3), dtype=np.uint8)

start_point = (100,100)
end_point = (200,200)

cv.rectangle(img, start_point, end_point, (255,255,255), -1)

tx, ty = 50,30
trnaslation_matrix = np.float32([[1,0,tx], [0,1,ty]])
translated = cv.warpAffine(img, trnaslation_matrix, (300,300))

center = (150,150)
angle = 45
sclae = 1.0
rotation_matrix = cv.getRotationMatrix2D(center, angle, sclae)
rotated = cv.warpAffine(translated, rotation_matrix, (300,300))



cv.imshow('Original Image', img)
cv.imshow('Translated Image', translated)
cv.imshow('Rotated Image', rotated)


cv.waitKey(0)
cv.destroyAllWindows()
