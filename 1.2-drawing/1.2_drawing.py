import cv2
import numpy as np
# 1 다양한 선 그리기

img = cv2.imread('/Users/kis/Documents/GitHub/Computer-vision-study/1.2-drawing/white.png')

# cv2.line(img, (50,50), (150,50), (255,0,0)) # x좌표 / y좌표 / (B, G, R)
# cv2.line(img, (100,350), (400,200), (0,0,255), 20, cv2.LINE_AA)
# cv2.line(img, (100,250), (400,300), (0,0,255), 20, cv2.LINE_4)

# cv2.rectangle() -> 매개변수들: img, 좌표(x,y), 너비높이(w,h), 색(B,G,R), 두께(20)
# cv2.rectangle(img, (60,40), (125,120), (255,0,0))

# 번개 모양 좌표
pts1 = np.array([[50,50], [150,150], [100,140], [200,240]], dtype = np.int32)
pts2 = np.array([[350,250], [450,350], [400,450], [300,450], [250,350]], dtype = np.int32)

cv2.polylines(img, [pts1], False, (255,0,0), 1, cv2.LINE_AA)
cv2.polylines(img, [pts2], True, (0,0,0), 1, cv2.LINE_AA)


cv2.imshow('polygons', img)
cv2.waitKey(0)
cv2.destroyAllWindows()