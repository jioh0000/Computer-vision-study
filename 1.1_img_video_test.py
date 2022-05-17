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



for i in range(1,101):
    img_file = f"/Users/kis/Documents/GitHub/Computer-vision-study/에스파윈터/에스파윈터{i}.jpg"
    save_file = f"/Users/kis/Documents/GitHub/Computer-vision-study/에스파윈터흑백/에스파윈터흑백{i}.jpg"
    
    img = cv2.imread(img_file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(save_file, gray)
    print(f"Completed: {i}")