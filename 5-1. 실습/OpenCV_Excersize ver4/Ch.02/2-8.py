import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

captured_images = []

print(" 'a'키 한 장 캡처, 'q키': 캡처 이미지 보기 및 종료 ")

while True:
    ret, frame = cap.read()
    if not ret:
        print('프레임을 가져올 수 없습니다. 종료합니다.')
        break

    cv.imshow('Live Video', frame)
    key = cv.waitKey(1) & 0xFF

    if key == ord('a'):
        captured_images.append(frame.copy())
        print(f"📸{len(captured_images)}번째 이미지 캡처됨")

    elif key == ord('q'):
        print(f"🖼️ 총{len(captured_images)}장의 이미지가 캡처되었습니다.")
        break

