import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5n')


def on_trackbar(val):
    global threshold
    threshold = val / 100

threshold = 0.2

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("카메라 오픈 에러")
    exit()

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

fourcc = cv2.VideoWriter_fourcc(*'XVID')  
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # 20fps, 640x480

title = "webcam YOLO Detection with Trackbar"
cv2.namedWindow(title)
cv2.createTrackbar("Min Confidence", title, int(threshold * 100), 100, on_trackbar)

while True:
    ret, frame = cam.read()
    
    if not ret:
        print("프레임 읽을 수 없음")
        break

    results = model(frame)
    df = results.pandas().xyxy[0]
        
    filtered = df[df['confidence'] >= threshold]
    
    for _, row in filtered.iterrows():
        xmin, ymin, xmax, ymax = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
        label = f"{row['name']} {row['confidence']:.2f}"

        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
        cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imshow(title, frame)
    
    # 'person'이 감지된 경우
    if not df[df['name'] == 'person'].empty:
        out.write(frame)
        
    if cv2.waitKey(1) == 27:  # ESC
        break



cam.release()
out.release()
cv2.destroyAllWindows()
