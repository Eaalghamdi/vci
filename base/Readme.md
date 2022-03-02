pip install --upgrade pip
pip install opencv-python-headless
pip install opencv-contrib-python
pip install imutils
python -m pip install -U scikit-image
pip install scenedetect
pip install ffmpeg-python
pip install pyinstaller

****TODO*****
before use pyinstaller
create api.spec file and
add this to api.spec --> datas=[ ('/Users/niccanordhasm/Documents/Untitled/base/src', 'src')]
Pyinstaller api.spec 

open before xcode
python3 -m venv /path/to/new/virtual/environment