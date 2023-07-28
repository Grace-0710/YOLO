import os
from pathlib import Path
from IPython.display import display
from PIL import Image

# 학습에 필요한 설정값들입니다.
data_dir = Path("data")  # 데이터 디렉토리 경로
print('데이타 경로::', data_dir)
video_dir = data_dir / "videos"  # 동영상 데이터 디렉토리 경로
video_path = video_dir / "sample_video.mp4"  # 학습에 사용할 동영상 경로
image_dir = data_dir / "images"  # 이미지 데이터 디렉토리 경로
image_dir.mkdir(exist_ok=True)  # 이미지 디렉토리 생성
annotation_file = data_dir / "annotations.txt"  # 어노테이션 파일 경로

# 동영상을 이미지로 변환하는 함수
def video_to_images(video_path, image_dir):
    os.system(f"ffmpeg -i {video_path} -vf fps=5 {image_dir/'%04d.jpg'}")

# YOLOv5 학습 함수
def train_yolov5(data_dir):
    os.system(f"python {data_dir}/yolov5/train.py --img 640 --batch 8 --epochs 50 --data {data_dir}/yolov5_data.yaml --cfg {data_dir}/yolov5s.yaml --weights yolov5s.pt --name yolov5s_results")

# YOLOv5 검증 함수
def validate_yolov5(data_dir):
    os.system(f"python {data_dir}/yolov5/val.py --img 640 --batch 8 --conf 0.001 --iou 0.65 --data {data_dir}/yolov5_data.yaml --weights {data_dir}/yolov5s_results/weights/best.pt")

# 동영상을 이미지로 변환합니다.
video_to_images(video_path, image_dir)

# 어노테이션 파일 생성 (이미지 파일명과 물체의 좌표 정보)
with open(annotation_file, "w") as f:
    for image_path in image_dir.glob("*.jpg"):
        f.write(f"{image_path} 0,0,100,100,0\n")  # 예시로 0,0,100,100,0으로 임의의 좌표 정보를 기록합니다.

# YOLOv5 학습 실행
train_yolov5(data_dir)

# YOLOv5 검증 실행
validate_yolov5(data_dir)
