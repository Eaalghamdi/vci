import os

import cv2
import numpy as np
import provider as Provider
# from skimage import metrics


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the sum of the squared difference between the two images
    mse_error = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    mse_error /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE. The lower the error, the more "similar" the two images are.
    return mse_error


def isBlack(crop):  # Function that tells if the crop is black
    mask = np.zeros(crop.shape, dtype=int)
    return not (np.bitwise_or(crop, mask)).any()


def compare(imageA, imageB):
    # This is the percentage of the width/height we're gonna cut
    # 0.99 < percent < 0.1
    percent = 0.01

    before = imageA
    after = imageB

    # Here, we eliminate the biggest differences between before and after
    result = after - before

    h, w, _ = result.shape

    hPercent = percent * h
    wPercent = percent * w

    for wFrom in range(0, w, int(wPercent)):  # Here we are gonna remove that noise
        for hFrom in range(0, h, int(hPercent)):
            wTo = int(wFrom+wPercent)
            hTo = int(hFrom+hPercent)
            crop = result[wFrom:wTo, hFrom:hTo]  # Crop the image

            if isBlack(crop):  # If it is black, there is no shot in it
                continue    # We dont need to continue with the algorithm

            beforeCrop = before[wFrom:wTo, hFrom:hTo]  # Crop the image before

            # If the image before is not black, it means there was a hot already there
            if not isBlack(beforeCrop):
                # So, we erase it from the result
                result[wFrom:wTo, hFrom:hTo] = [0, 0, 0]

    return result


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
            mse_value = np.mean(mse(gray1, gray2).astype("uint8"))
            ssim_value = np.std(compare(image1, image2).astype("uint8"))

            imgf1 = os.path.basename(f1)
            imgf2 = os.path.basename(f2)
            imgNameF1 = imgf1.split(".")[0]
            imgNameF2 = imgf2.split(".")[0]

            Provider.insert_structsimilarity(
                [imgNameF1, imgNameF2, mse_value, ssim_value])

    return 'completed'
