import cv2
import os
import provider as Provider


def object_detection(frameDir, thrHold):
    imgs = []

    if Provider.clear_objectdetection() == 'completed':
        for x in os.listdir(frameDir):
            if x.endswith(".jpg"):
                imgs.append(frameDir + '/' + x)

    for img in imgs:
        config_file = '/Users/niccanordhasm/auvana_v_1/base/FeatureExtraction/src/object_detection/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
        frozen_model = '/Users/niccanordhasm/auvana_v_1/base/FeatureExtraction/src/object_detection/frozen_inference_graph.pb'
        coco = '/Users/niccanordhasm/auvana_v_1/base/FeatureExtraction/src/object_detection/coco.txt'
        # imgss = '/Users/niccanordhasm/auvana_v_1/tmp/sample-mp4-file/shot1335.jpg'

        model = cv2.dnn_DetectionModel(frozen_model, config_file)
        model.setInputSize(320, 320)
        model.setInputScale(1.0/127.5)
        model.setInputMean((127.5, 127.5, 127.5))
        model.setInputSwapRB(True)

        classLabels = []

        with open(coco, 'rt') as fpt:
            classLabels = fpt.read().rstrip('\n').split('\n')
            classLabels.append(fpt.read())

        imgFinal = cv2.imread(img)
        # cv2.imshow('', imgFinal)

        ClassIndex, confidence, bbox = model.detect(
            imgFinal, confThreshold=thrHold)
        # for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
        #     cv2.rectangle(imgFinal, boxes, (255,0,0),2)
        # cv2.imshow('', cv2.cvtColor(imgFinal, cv2.COLOR_BGR2RGB))
        # cv2.waitKey(0)
        Provider.insert_objectdetection(
            [ClassIndex, confidence, bbox])

        return 'completed'

