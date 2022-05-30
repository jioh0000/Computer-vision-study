import numpy as np
import cv2

win_name = "Trackbar"

img = cv2.imread('/Users/kis/Documents/GitHub/Computer-vision-study/1.3-trackbar/white.png')
cv2. imshow(win_name, img)

# 트렉바 이벤트 처리 함수 선어
def onChange(x):
    print(x)
    # R,G,B 각 트렉바 위치
    r = cv2.getTrackbarPos('R', win_name)
    g = cv2.getTrackbarPos('G', win_name)
    b = cv2.getTrackbarPos('B', win_name)
    print(r,g,b)
    img[:] = [b,g,r]
    cv2.imshow(win_name, img)

# 트렉바 생성
cv2.createTrackbar('R', win_name, 255,255, onChange)
cv2.createTrackbar('G', win_name, 255,255, onChange)
cv2.createTrackbar('B', win_name, 255,255, onChange)

while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()