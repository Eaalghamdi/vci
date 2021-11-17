
import cv2
import os
from statistics import mean, variance, stdev


class Processing:
    def __init__(self, video):
        self.video = video
        # self.cwd = os.getcwd()

    # @staticmethod
    def read(self):
        cap = cv2.VideoCapture(self.video)
        return cap

### STATS ###
    def get_fbs(self):
        cap = self.read()
        fps = cap.get(cv2.CAP_PROP_FPS)
        return fps

    def get_frameCounts(self):
        cap = self.read()
        frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        return frame_count

    def get_dimesnion(self):
        cap = self.read(self.video)
        width = cap.get(3)  # float
        height = cap.get(4)  # float
        return (width, height)

    def get_duration(self):
        pass

    def get_summary(self):
        cap = self.read()
        frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
        print(width, height, frame_count, fps)

### RESOLUTION ###

    def change_resolution(self, percent):
        pass

    def get_extraxted_frames(self):
        print(self.cwd)

    def safe_divide(numerator, denominator):
        if denominator == 0:
            index = 0
        else:
            index = numerator/denominator
        return index

    # helping function
    def sortedFrames(listFrames):
        listFrames = [x.split('.')[0] for x in listFrames]
        listFrames = sorted(listFrames, key=lambda x: int(x))
        listFrames = [x + '.jpg'for x in listFrames]
        return listFrames

# ff = Processing()
# gg = ff.read()
# gg.make_720p()


# filename = Path("functions/motionSalincy.py")

# # Convert path to Windows format
# path_on_windows = PureWindowsPath(filename)
# print(path_on_windows)
