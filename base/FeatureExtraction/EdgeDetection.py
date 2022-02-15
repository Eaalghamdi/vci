import cv2


def edge_detection(img):
    # Read the original image
    img = cv2.imread(img)

    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

    # # Sobel Edge Detection
    # sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1,
    #                    dy=0, ksize=5)  # Sobel Edge Detection on the X axis
    # sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0,
    #                    dy=1, ksize=5)  # Sobel Edge Detection on the Y axis
    # # Combined X and Y Sobel Edge Detection
    # sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

    # Canny Edge Detection
    edges = cv2.Canny(image=img_blur, threshold1=100,
                      threshold2=200)  # Canny Edge Detection

    saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
    (success, saliencyMap) = saliency.computeSaliency(img)
    saliencyMap = (saliencyMap * 255).astype("uint8")
    # print(saliencyMap)
    # cv2.imshow('Original', edges)
    # cv2.waitKey(0)


# edge_detection(
#     '/Users/niccanordhasm/Documents/GitHub/auvana_v_1/tmp/file_example_MP4_640_3MG/shot0.jpg')


# import pandas as pd
# import cv2
# import glob
# from utities import Processing
# import os


# class EdgeDetection(Processing):
#     def __init__(self, video):
#         super(). __init__(video)

#     cols = ['frame', 'canny_size']
#     results = []

#     def cannyImg(self, frame, width, height):
#         file_name = "canny" + frame
#         img = cv2.imread(img, 0)
#         dim = (width, height)
#         fream_resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
#         edges = cv2.Canny(fream_resized, 100, 150)
#         cv2.imwrite(file_name, edges)
#         canny_size = os.path.getsize(file_name)
#         results.append([file_name, canny_size])
#         os.remove(file_name)

#     def start(self, features=None):
#         self.get_extraxted_frame()


# d = Functions('GA18.mp4')


# imgs = [img for img in glob.glob("test_imgs/*.jpeg")]

# for image in imgs:
#     imgName = image.split('.')[0]
#     imgName = image.split('/')[1]

#     img = cv2.imread(image)
#     saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
#     (success, saliencyMap) = saliency.computeSaliency(img)
#     saliencyMap = (saliencyMap * 255).astype("uint8")

#     out_name = "SpectralResidual_" + imgName
#     cv2.imwrite(out_name, saliencyMap)

# for img in imgs:
#     # cap = cv2.imread(img)
#     # dim = (320, 240)
#     # fream_resized = cv2.resize(cap, dim, interpolation = cv2.INTER_AREA)
#     # cv2.imwrite(img, fream_resized)

# help(cv2.saliency.StaticSaliencyFineGrained_create())
