yolo project

setting
1. anaconda 환경설정
2. pycharm terminal cmd로 변경
3. 코드 작성
   
- conda install cmake ninja
- pip install -r requirements.txt
- conda install mkl mkl-include
- conda install -c conda-forge libuv=1.39
  
- git clone --recursive https://github.com/pytorch/pytorch
- cd pytorch
- git submodule sync
- git submodule update --init --recursive
- conda activate
- python setup.py develop

- git clone https://github.com/ultralytics/yolov5
- cd yolov5
- pip install -r requirements.txt
