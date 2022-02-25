import json
import os
import shutil

import cv2
from scenedetect.detectors import ContentDetector, ThresholdDetector
from scenedetect.scene_manager import SceneManager
from scenedetect.stats_manager import StatsManager
from scenedetect.video_manager import VideoManager


def shot_bundry_detection(videoPath, videoFileName, method, treshold, defaultH, defaultW):

    videoFolderName = str(videoFileName).split('.', 1)[0]
    pathOfDest = videoPath + "/" + videoFolderName

    if os.path.isdir(pathOfDest):
        shutil.rmtree(pathOfDest)
        createDir(videoPath, videoFolderName)
        process(videoPath, videoFileName, method,
                treshold, pathOfDest, defaultH, defaultW)
        json_output = json.dumps(
            {'error': 'false', 'data': 'completed'})
        return json_output
    else:
        createDir(videoPath, videoFolderName)
        process(videoPath, videoFileName, method,
                treshold, pathOfDest, defaultH, defaultW)
        json_output = json.dumps(
            {'error': 'false', 'data': 'completed'})
        return json_output


def createDir(videoPath, videoFolderName):
    os.makedirs(videoPath + "/" + videoFolderName, exist_ok=True)


def process(videoPath, videoFileName, method, treshold, pathOfDest, defaultH, defaultW):
    video_manager = VideoManager([videoPath + "/" + videoFileName])
    stats_manager = StatsManager()
    scene_manager = SceneManager(stats_manager)

    # Add ContentDetector algorithm (constructor takes detector options like threshold).
    if method == 'ContentDetector':
        scene_manager.add_detector(ContentDetector(float(treshold)))
    if method == 'threshold_detector':
        scene_manager.add_detector(ThresholdDetector(int(treshold)))

    base_timecode = video_manager.get_base_timecode()

    # Set downscale factor to improve processing speed (no args means default).
    video_manager.set_downscale_factor()

    # Start video_manager.
    video_manager.start()

    # Perform scene detection on video_manager.
    scene_manager.detect_scenes(frame_source=video_manager)

    # Obtain list of detected scenes.
    scene_list = scene_manager.get_scene_list(base_timecode)

    cap = cv2.VideoCapture(videoPath + "/" + videoFileName)

    for i, scene in enumerate(scene_list):
        i = i+1
        cut_frame = scene[0].get_frames()
        cap.set(1, cut_frame)
        ret, frame = cap.read()
        frame_name = "shot " + str(i) + ".jpg"
        cv2.imwrite(pathOfDest + "/" + frame_name, cv2.resize(frame, (defaultH, defaultW),
                                                              interpolation=cv2.INTER_NEAREST))

    cap.release()
    cv2.destroyAllWindows()

    # sort the list of imnags in dic as they saved
    # imgs = sorted(glob.glob('*.jpg'), key=os.path.getmtime)
