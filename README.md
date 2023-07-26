<h1>yolo project</h1>

<h2>setting</h2>
<div>1. anaconda 환경설정</div>
<div>환경변수 path에 추가</div>
<div>anaconda3</div>
<div>anaconda3\Library</div>
<div>anaconda3\Scripts</div>
<br>
<div>2. pycharm terminal cmd로 변경</div>
<br>
<div>3. 코드 작성</div>
<div>- conda install cmake ninja</div>
<div>- pip install -r requirements.txt</div>
<div>- conda install mkl mkl-include</div>
<div>- conda install -c conda-forge libuv=1.39</div>
<br>
<div>- git clone --recursive https://github.com/pytorch/pytorch</div>
<div>- cd pytorch</div>
<div>- git submodule sync</div>
<div>- git submodule update --init --recursive</div>
<div>- conda activate</div>
<div>- python setup.py develop</div>
<br>
<div>- git clone https://github.com/ultralytics/yolov5</div>
<div>- cd yolov5</div>
<div>- pip install -r requirements.txt</div>
