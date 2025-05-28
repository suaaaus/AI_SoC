import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5n')
# print(model)
# print(torch.__version__)

img_path = '/home/pi/yolov5/data/images/bus.jpg' 
img = cv2.imread(img_path)

results = model(img)
df = results.pandas().xyxy[0]

def on_trackbar(val):
    global threshold
    threshold = val / 100

threshold = 0.2

title = "Yolo Detection with Trackbar"
cv2.namedWindow(title)
cv2.createTrackbar("Min Confidence", title, int(threshold * 100), 100, on_trackbar)

while True:
   
    display_img = img.copy()

    filtered = df[df['confidence'] >= threshold]

    for _, row in filtered.iterrows():
        xmin, ymin, xmax, ymax = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
        label = f"{row['name']} {row['confidence']:.2f}"

        cv2.rectangle(display_img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
        cv2.putText(display_img, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imshow(title, display_img)

    key = cv2.waitKey(30)
  
    if key == 27:  # ESC
        break

cv2.destroyAllWindows()
