import cv2
import numpy as np
import os
import provider as Provider


def edge_detection(frameDir, mode, submode, thrHold1, thrHold2):
    imgs = []

    if Provider.clear_edgedetection() == 'completed':
        for x in os.listdir(frameDir):
            if x.endswith(".jpg"):
                imgs.append(frameDir + '/' + x)

    if mode == 'static':
        if submode == 'spectral':
            for img in imgs:
                # Read the original image
                img = cv2.imread(img)

                # initialize OpenCV's static saliency spectral residual detector and
                # compute the saliency map
                saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
                (success, saliencyMap) = saliency.computeSaliency(img)

                mapss = (saliencyMap * 255).astype("uint8")

                # caculate and add all results
                mean_color = np.mean(mapss)
                std_color = np.std(mapss)

                mean_adj_abs = np.mean(abs(mapss))
                std_adj_abs = np.std(abs(mapss))

                Provider.insert_edgedetection(
                    [mean_color, std_color, mean_adj_abs, std_adj_abs])

            return 'completed'

        elif submode == 'finegrained':
            for img in imgs:
                # Read the original image
                img = cv2.imread(img)

                # initialize OpenCV's static fine grained saliency detector and
                # compute the saliency map
                saliency = cv2.saliency.StaticSaliencyFineGrained_create()
                (success, saliencyMap) = saliency.computeSaliency(img)

                mapss = (saliencyMap * 255).astype("uint8")

                # caculate and add all results
                mean_color = np.mean(mapss)
                std_color = np.std(mapss)

                mean_adj_abs = np.mean(abs(mapss))
                std_adj_abs = np.std(abs(mapss))

                Provider.insert_edgedetection(
                    [mean_color, std_color, mean_adj_abs, std_adj_abs])

            return 'completed'

        elif submode == 'canny':
            for img in imgs:
                # Read the original image
                img = cv2.imread(img)

                # Convert to graycsale
                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # Blur the image for better edge detection
                img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

                # Canny Edge Detection
                edges = cv2.Canny(image=img_blur, threshold1=thrHold1,
                                threshold2=thrHold2)  

                mapss = (edges * 255).astype("uint8")

                # caculate and add all results
                mean_color = np.mean(mapss)
                std_color = np.std(mapss)

                mean_adj_abs = np.mean(abs(mapss))
                std_adj_abs = np.std(abs(mapss))

                Provider.insert_edgedetection(
                    [mean_color, std_color, mean_adj_abs, std_adj_abs])
            
            return 'completed'



edge_detection(
    '/Users/niccanordhasm/auvana_v_1/tmp/sample-mp4-file/shot0.jpg', 'static', 'spectral', 50, 50)



