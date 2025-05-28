import cv2

def on_trackbar(val):
    global minVal
    minVal = val

minVal = 50
maxVal = 150  

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("카메라 오픈 에러")
    exit()

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


title = "Canny Edge with Trackbar"
cv2.namedWindow(title)
cv2.createTrackbar("Min Threshold", title, minVal, 255, on_trackbar)

while True:
    ret, frame = cam.read()
    if not ret:
        print("프레임을 읽을 수 없음")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, minVal, maxVal)

    cv2.imshow(title, edges)

    if cv2.waitKey(1) == 27:  
        break


cam.release()
cv2.destroyAllWindows()
