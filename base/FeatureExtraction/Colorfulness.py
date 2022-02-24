import json
import cv2
import numpy as np
import os
import provider as Provider


# Code Credit: https://www.pyimagesearch.com/2017/06/05/computing-image-colorfulness-with-opencv-and-python/


def colorfulness(image):
    try:
        # split the image into its respective RGB components
        (B, G, R) = cv2.split(image.astype("float"))

        # compute rg = R - G
        rg = np.absolute(R - G)

        # compute yb = 0.5 * (R + G) - B
        yb = np.absolute(0.5 * (R + G) - B)

        # compute the mean and standard deviation of both `rg` and `yb`
        (rbMean, rbStd) = (np.mean(rg), np.std(rg))
        (ybMean, ybStd) = (np.mean(yb), np.std(yb))

        # combine the mean and standard deviations
        stdRoot = np.sqrt((rbStd ** 2) + (ybStd ** 2))
        meanRoot = np.sqrt((rbMean ** 2) + (ybMean ** 2))

        # derive the "colorfulness" metric and return it
        return stdRoot + (0.3 * meanRoot)
    except Exception as e:
        pass


# mode == 0 is single, mode == 1 is multiple
def get_colorfulness(frameDir, mode):
    imgs = []
    if Provider.clear_colorfulness() == 'completed':
        for x in os.listdir(frameDir):
            if x.endswith(".jpg"):
                imgs.append(frameDir + '/' + x)

        if mode == 0:
            for img in imgs:
                img = cv2.imread(img, cv2.IMREAD_UNCHANGED)

                img1_color = colorfulness(img)

                # caculate and add all results
                mean_color = np.mean(img)
                std_color = np.std(img)

                mean_adj = np.mean(img1_color)
                std_adj = np.std(img1_color)

                mean_adj_abs = np.mean(abs(img1_color))
                std_adj_abs = np.std(abs(img1_color))

                Provider.insert_colorfulness(
                    [img1_color, mean_color, std_color, mean_adj, std_adj, mean_adj_abs, std_adj_abs])

            return 'completed'

        elif mode == 1:
            for f1, f2 in zip(imgs, imgs[1:]):

                f1 = cv2.imread(f1, cv2.IMREAD_UNCHANGED)
                f2 = cv2.imread(f2)

                width = int(f1.shape[1])
                height = int(f1.shape[0])
                dim = (width, height)
                # resize image
                f2 = cv2.resize(f2, dim, interpolation=cv2.INTER_AREA)

                img1_color = colorfulness(f1)
                img2_color = colorfulness(f2)

                # caculate and add all results
                mean_color = np.mean(f1)
                std_color = np.std(f1)

                mean_adj = np.mean(img1_color - img2_color)
                std_adj = np.std(img1_color - img2_color)

                mean_adj_abs = np.mean(abs(img1_color - img2_color))
                std_adj_abs = np.std(abs(img1_color - img2_color))

                Provider.insert_colorfulness(
                    [img1_color, mean_color, std_color, mean_adj, std_adj, mean_adj_abs, std_adj_abs])

            return 'completed'
