import cv2

# 1 이미지 파일을 화면에 표시하는 법

# img_file = "img.png"
# img  = cv2.imread(img_file)

# print(img)

# if img is not None:
#     cv2.imshow('image-test', img)
#     cv2.waitKey() # 키가 입력될 때 까지 대기
#     cv2.destroyAllWindows() # 화면 끄기
# else:
#     print("No image file")


# 2 이미지 파일을 그레이 스케일러 화면에 표시 -> 흑백

# img_file = "img.png"
# img  = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE) # 두번째 매개변수에는 색을 정할 수 있음

#print(img)

# cv2.imshow('img', img)
# cv2.waitKey()
# cv2.destroyAllWindows()


# 3 컬러(원본) 이미지를 그레이스케일로 변환하여 저장

# img_file = "img.png"
# save_file = "grayscaled_img.png"

# img  = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
# cv2.imshow(img_file, img)
# cv2.imwrite(save_file, img) # 1번쨰 매개변수: 파일이름 및 경로, 2번째 매개변수: 저장할 이미지변수
# cv2.waitKey()
# cv2.destroyAllWindows()


# 4 많은 컬러(원본) 이미지를 그레이스케일로 변환하여 저장

# for i in range(1,101):
#     img_file = f"/Users/kis/Documents/GitHub/Computer-vision-study/에스파윈터/에스파윈터{i}.jpg"
#     save_file = f"/Users/kis/Documents/GitHub/Computer-vision-study/에스파윈터흑백/에스파윈터흑백{i}.jpg"
    
#     img = cv2.imread(img_file)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     cv2.imwrite(save_file, gray)
#     print(f"Completed: {i}")


# 5 영상 출력
# video_file = '/Users/kis/Documents/GitHub/Computer-vision-study/test.mp4'
# capture = cv2.VideoCapture(video_file)

# while True:
#     ret, img =  capture.read() # 다음 프레음 읽기  img는 카마라가 보는 각각의 프레임 / 양상은 사진의 빠른 나열
#     if ret: # True: 카메라 오픈, False: 카메라 없음
#         cv2.imshow(video_file, img)
#         cv2.waitKey(25) # 25mls 지연 --> 약 40fps
#     else:
#         break

# capture.release() # 캡쳐 자원 반납 / 비디오 끄기
# cv2.destroyAllWindows()


# 6 카메라로 사진 찍기
# cap = cv2.VideoCapture(0)

# if cap.isOpened():
#     while True:
#         _, frame = cap.read()
    
#         cv2.imshow("camera", frame)
#         if cv2.waitKey(1) != -1: # 아무키나 누르면 
#             cv2.imwrite('photo.jpg', frame)
#             break
# cap.release()
# cv2.destroyAllWindows()


# 7 카메라로 녹화하기
cap = cv2.VideoCapture(0)

if cap.isOpened():
    file_path = "record.avi"
    fps = 25.40
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height)) # frame 크기
    out = cv2.VideoWriter(file_path, fourcc, fps, size) # 비디오 writer 객체 생성 // 저장할 파일 이름, 4글자 인코딩, fps, 프레임 사이즈

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('cam-record', frame)
            out.write(frame)
            if cv2.waitKey(int(1000/fps)) != 1:
                break
        else:
            break
    out.release()
else:
    print("no cam")
cap.release()
cv2.destroyAllWindows()