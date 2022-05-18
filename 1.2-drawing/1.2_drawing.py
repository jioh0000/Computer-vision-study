import cv2

# 1 다양한 선 그리기

img = cv2.imread('/Users/kis/Documents/GitHub/Computer-vision-study/1.2-drawing/white.png')

cv2.line(img, (50,50), (150,50), (255,0,0)) # x좌표 / y좌표 / (B, G, R)
cv2.line(img, (100,350), (400,200), (0,0,255), 20, cv2.LINE_AA)
cv2.line(img, (100,250), (400,300), (0,0,255), 20, cv2.LINE_4)

cv2.imshow('lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()