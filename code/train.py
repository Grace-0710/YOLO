#dataset : https://hansonminlearning.tistory.com/71 참고하여 만듬
# 참고 : https://blog.naver.com/PostView.naver?blogId=beyondlegend&logNo=223050797442
# Load YOLOv8n

from ultralytics import YOLO

model = YOLO('yolov8n.pt')
print(type(model.names), len(model.names))
print(model.names)
model.train(data='./data.yaml', epochs=100, patience=30, batch=32, imgsz=416)