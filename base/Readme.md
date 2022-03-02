pip install --upgrade pip
pip3 install opencv-python-headless
pip3 install opencv-contrib-python
pip3 install imutils
pip install scikit-image (latest - 0.19 use pip only for this)
pip3 install scenedetect
pip3 install ffmpeg-python
pip3 install pyinstaller

****TODO*****
before use pyinstaller
create api.spec file and
add this to api.spec --> datas=[ ('/Users/niccanordhasm/Documents/Untitled/base/src', 'src')]
Pyinstaller api.spec 

python3 -m venv /path/to/new/virtual/environment