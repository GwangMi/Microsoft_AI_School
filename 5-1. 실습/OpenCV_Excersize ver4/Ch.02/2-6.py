import cv2 as cv

def draw(event, x, y, flags, param):
    global drawing_left, drawing_right, img

    if event == cv.EVENT_LBUTTONDOWN:
        drawing_left = True

    elif event == cv.EVENT_MOUSEMOVE and drawing_left:
        cv.circle(img, (x,y),5,(255,0,0),  -1)
    
    elif event == cv.EVENT_LBUTTONUP:
        drawing_left = False
    
    elif event == cv.EVENT_RBUTTONDOWN:
        drawing_right = True
    
    elif event == cv.EVENT_MOUSEMOVE and drawing_right:
        cv.circle(img, (x,y), 5, (0,0,255),-1)
    
    elif event == cv.EVENT_RBUTTONUP:
        drawing_right = False

img = cv.imread('Ch.02\soccer2.jpg')
if img is None:
    print('이미지를 불러올 수 없습니다.')
    exit()


drawing_left = False
drawing_right = False

cv.namedWindow('Draw Circles')
cv.setMouseCallback('Draw Circles', draw)

while True:
    cv.imshow('Draw Circles', img)
    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

cv.destroyAllWindows








