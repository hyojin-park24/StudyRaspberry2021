import cv2

cam = cv2.VideoCapture(0)   #0번 : 기본카메라
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  #창 넓이
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240) #창 높이

while True:
    ret, frame = cam.read() #웹캠 읽기

    if ret:
        cv2.imshow('Original Video', frame)    #카메라 영상 CAM이라는 이름으로 창에 띄움 

        key = cv2.waitKey(1)

        if key == ord('q'):  #q를 입력 받으면
            break

cam.release()
cv2.destroyAllWindows()
