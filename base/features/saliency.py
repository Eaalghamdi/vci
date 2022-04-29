import cv2
import numpy as np
import os
import provider as Provider


def saliency(frameDir):
    imgs = []
    # load the input image
    if Provider.clear_saliency() == 'completed':
        for x in os.listdir(frameDir):
            if x.endswith(".jpg"):
                imgs.append(frameDir + '/' + x)

        for imgq in imgs:
            image = cv2.imread(imgq)

            # initialize OpenCV's static saliency spectral residual detector and
            # compute the saliency map
            saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
            (success, saliencyMap) = saliency.computeSaliency(image)
            saliencyMas = (saliencyMap * 255).astype("uint8")

            # if we would like a *binary* map that we could process for contours,
            # compute convex hull's, extract bounding boxes, etc., we can
            # additionally threshold the saliency map
            threshMap = cv2.threshold(saliencyMas.astype("uint8"), 0, 255,
                                      cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

            mean = np.mean(threshMap.astype("uint8"))
            std = np.std(threshMap.astype("uint8"))

            imgNam = os.path.basename(imgq)
            imgName = imgNam.split(".")[0]

            Provider.insert_saliency(
                [imgName, mean, std])

        return 'completed'
