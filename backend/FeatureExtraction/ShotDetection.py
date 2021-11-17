import cv2
import scenedetect
from pathlib import Path, PureWindowsPath
from scenedetect.video_manager import VideoManager
from scenedetect.scene_manager import SceneManager
from scenedetect.frame_timecode import FrameTimecode
from scenedetect.stats_manager import StatsManager
from scenedetect.detectors import ContentDetector, ThresholdDetector


class ShotDetection:

    def detect_shots(video, method, treshold=30):

        video_manager = VideoManager([video])
        stats_manager = StatsManager()
        scene_manager = SceneManager(stats_manager)

        # Add ContentDetector algorithm (constructor takes detector options like threshold).
        if method == 'ContentDetector':
            scene_manager.add_detector(ContentDetector(treshold))
        if method == 'threshold_detector':
            scene_manager.add_detector(ThresholdDetector(treshold))

        base_timecode = video_manager.get_base_timecode()

        # Set downscale factor to improve processing speed (no args means default).
        video_manager.set_downscale_factor()

        # Start video_manager.
        video_manager.start()

        # Perform scene detection on video_manager.
        scene_manager.detect_scenes(frame_source=video_manager)

        # Obtain list of detected scenes.
        scene_list = scene_manager.get_scene_list(base_timecode)

        cap = cv2.VideoCapture(video)

        for i, scene in enumerate(scene_list):
            i = i+1
            cut_frame = scene[0].get_frames()
            cap.set(1, cut_frame)
            ret, frame = cap.read()
            frame_name = "shot " + str(i) + ".jpg"
            cv2.imwrite(frame_name, frame)

        # sort the list of imnags in dic as they saved
        # imgs = sorted(glob.glob('*.jpg'), key=os.path.getmtime)
