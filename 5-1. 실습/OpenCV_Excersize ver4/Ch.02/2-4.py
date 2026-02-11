import cv2 as cv
import sys

img = cv.imread('Ch.02/girl.jpg')


if img is None:
    sys.exit('File Not Found')


cv.rectangle(img, (330,470) ,(530,640), color=(255,0,0),thickness=3)

cv.putText(img, 'Hello OpenCV', org=(330,450), fontFace=cv.FONT_HERSHEY_SIMPLEX, 
                                     fontScale=1, color=(0,255,0), thickness=2)


cv.imshow('Image Display', img)


cv.imwrite('Ch.02\soccer.jpg', img)

cv.waitKey()

cv.destroyWindow()


