import cv2
import os
import provider as Provider


def facedetection(frameDir, minNeig, mode):
    
    imgs = []

    if Provider.clear_facedetection() == 'completed':
        for x in os.listdir(frameDir):
            if x.endswith(".jpg"):
                imgs.append(frameDir + '/' + x)

    face_cascade = cv2.CascadeClassifier(
        "/Users/niccanordhasm/auvana_v_1/base/src/face_detection/haarcascade_frontalface_default.xml")

    for frame in imgs:
        img = cv2.imread(frame)
        # convert to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray_img, scaleFactor=1.05, minNeighbors=minNeig)

        for x, y, w, h in faces:
            img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        # resised = cv2.resize(img, (int(img.shape[1]), (int(img.shape[0]))))
        numberFaces = len(faces)

        head, tail = os.path.split(frame)

        Provider.insert_facedetection(
            [tail, numberFaces])

    return 'completed'

