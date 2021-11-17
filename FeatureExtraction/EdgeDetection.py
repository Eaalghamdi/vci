import pandas as pd
import cv2
import glob
from utities import Processing
import os


class EdgeDetection(Processing):
    def __init__(self, video):
        super(). __init__(video)

    cols = ['frame', 'canny_size']
    results = []

    def cannyImg(self, frame, width, height):
        file_name = "canny" + frame
        img = cv2.imread(img, 0)
        dim = (width, height)
        fream_resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        edges = cv2.Canny(fream_resized, 100, 150)
        cv2.imwrite(file_name, edges)
        canny_size = os.path.getsize(file_name)
        results.append([file_name, canny_size])
        os.remove(file_name)

    def start(self, features=None):
        self.get_extraxted_frame()


d = Functions('GA18.mp4')


imgs = [img for img in glob.glob("test_imgs/*.jpeg")]

for image in imgs:
    imgName = image.split('.')[0]
    imgName = image.split('/')[1]

    img = cv2.imread(image)
    saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
    (success, saliencyMap) = saliency.computeSaliency(img)
    saliencyMap = (saliencyMap * 255).astype("uint8")

    out_name = "SpectralResidual_" + imgName
    cv2.imwrite(out_name, saliencyMap)

# for img in imgs:
#     # cap = cv2.imread(img)
#     # dim = (320, 240)
#     # fream_resized = cv2.resize(cap, dim, interpolation = cv2.INTER_AREA)
#     # cv2.imwrite(img, fream_resized)

# help(cv2.saliency.StaticSaliencyFineGrained_create())
