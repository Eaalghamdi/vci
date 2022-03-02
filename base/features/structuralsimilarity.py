import os

import cv2
import numpy as np
import provider as Provider
from skimage import metrics


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the sum of the squared difference between the two images
    mse_error = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    mse_error /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE. The lower the error, the more "similar" the two images are.
    return mse_error


def compare(imageA, imageB):
    # Calculate the MSE and SSIM
    m = mse(imageA, imageB)
    s = metrics.structural_similarity(imageA, imageB)

    # Return the SSIM. The higher the value, the more "similar" the two images are.
    return s


def strctural_similarity(frameDir):
    imgs = []
    if Provider.clear_structsimilarity() == 'completed':
        for x in os.listdir(frameDir):
            if x.endswith(".jpg"):
                imgs.append(frameDir + '/' + x)

    for f1, f2 in zip(imgs, imgs[1:]):
        # Import images
        image1 = cv2.imread(f1)
        image2 = cv2.imread(f2, 1)

        # Convert the images to grayscale
        gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

        # Check for same size and ratio and report accordingly
        ho, wo, _ = image1.shape
        hc, wc, _ = image2.shape
        ratio_orig = ho/wo
        ratio_comp = hc/wc
        dim = (wc, hc)

        if round(ratio_orig, 2) != round(ratio_comp, 2):
            # Images not of the same dimension. Check input
            exit()

        # Resize first image if the second image is smaller
        elif ho > hc and wo > wc:
            gray1 = cv2.resize(gray1, dim)

        elif ho < hc and wo < wc:
            # Compressed image has a larger dimension than the original. Check input.
            exit()

        if round(ratio_orig, 2) == round(ratio_comp, 2):
            mse_value = mse(gray1, gray2)
            ssim_value = compare(gray1, gray2)

            imgf1 = os.path.basename(f1)
            imgf2 = os.path.basename(f2)
            imgNameF1 = imgf1.split(".")[0]
            imgNameF2 = imgf2.split(".")[0]

            Provider.insert_structsimilarity(
                [imgNameF1, imgNameF2, mse_value, ssim_value])

    return 'completed'
