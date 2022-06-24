import cv2 
import numpy as np 

thresh = 25
max_diff = 5 

a, b, c = None, None, None

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

if cap.isOpened():
    ret, a = cap.read()

    ret, b = cap.read()

    while ret:
        ret, c = cap.read()
        draw = c.copy()
        if not ret:
            break 

        a_gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
        b_gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
        c_gray = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)

        diff1 = cv2.absdiff(a_gray, b_gray)
        diff2 = cv2.absdiff(b_gray, c_gray)

        # 스레시홀드로 기준치 이내의 차이는 무시하라 
        ret, diff1_t = cv2.threshold(diff1, thresh, 255, cv2.THRESH_BINARY)
        ret, diff2_t = cv2.threshold(diff2, thresh, 255, cv2.THRESH_BINARY)

        # 두 차이에 대해서 AND연산, 두 Frame의 차이가 모두 발견된 경우에만 True 
        diff = cv2.bitwise_and(diff1_t, diff2_t)

        # 노이즈 제거 하기 
        k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
        diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)

        # 모션이 발생 한 픽셀의 개수를 판단하고 사각형 그리기 
        diff_cnt = cv2.countNonZero(diff)
        if diff_cnt > max_diff:
            nzero = np.nonzero(diff) # 0이 아니였던 픽셀들의 위치를  얻을 수 있음 
            cv2.rectangle(draw, (min(nzero[1]), min(nzero[0]), max(nzero[1]), max(nzero[0])), (0, 255, 0), 2)
            cv2.putText(draw, "Motion Detected", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
        
        # 컬러 스케일 영상과 스레시홀드 영상을 통합해서 출력
        stacked = np.hstack((draw, cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)))
        cv2.imshow("motion cctv", stacked)

        # 다음 비교를 위해 순서 정리
        a = b
        b = c

        if cv2.waitKey(1) & 0xFF == 27:
            break