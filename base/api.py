import provider as Provider
import sys
import database.db as DB


if __name__ == '__main__':
    if sys.argv[1] == 'init':
        print(DB.init())
        sys.stdout.flush()
    elif sys.argv[1] == 'get_projects':
        print(Provider.get_projects())
        sys.stdout.flush()
    elif sys.argv[1] == 'get_project':
        data = [sys.argv[2]]
        print(Provider.get_project(data))
        sys.stdout.flush()
    elif sys.argv[1] == 'create_project':
        data = [sys.argv[2], sys.argv[3], sys.argv[4]]
        print(Provider.create_project(data))
        sys.stdout.flush()
    elif sys.argv[1] == 'delete_project':
        id = [sys.argv[2]]
        print(Provider.delete_project(id))
        sys.stdout.flush()
    elif sys.argv[1] == 'shot_bundry_detection':
        videoPath = sys.argv[2]
        videoFileName = sys.argv[3]
        method = sys.argv[4]
        treshold = sys.argv[5]
        defaultW = int(sys.argv[6])
        defaultH = int(sys.argv[7])
        print(Provider.fe_shot_boundry_det(
            videoPath, videoFileName, method, treshold, defaultH, defaultW))
        sys.stdout.flush()
    elif sys.argv[1] == 'manual_frame':
        videoPath = sys.argv[2]
        videoFileName = sys.argv[3]
        time = sys.argv[4]
        defaultW = int(sys.argv[5])
        defaultH = int(sys.argv[6])
        print(Provider.fe_manual_frame(
            videoPath, videoFileName, time, defaultH, defaultW))
        sys.stdout.flush()
    elif sys.argv[1] == 'colorfulness':
        imgsPath = sys.argv[2]
        imgsMode = int(sys.argv[3])
        print(Provider.colorfulness(imgsPath, imgsMode))
        sys.stdout.flush()
    elif sys.argv[1] == 'get_colorfulness':
        print(Provider.get_colorfulness())
        sys.stdout.flush()
    elif sys.argv[1] == 'edgedetection':
        frameDir = sys.argv[2]
        mode = sys.argv[3]
        submode = sys.argv[4]
        thrHold1 = int(sys.argv[5])
        thrHold2 = int(sys.argv[6])
        print(Provider.edgedetection(frameDir, mode, submode, thrHold1, thrHold2))
        sys.stdout.flush()
    elif sys.argv[1] == 'get_edgedetection':
        print(Provider.get_edgedetection())
        sys.stdout.flush()
    elif sys.argv[1] == 'objectdetection':
        frameDir = sys.argv[2]
        thrHold = float(sys.argv[3])
        print(Provider.objectdetection(frameDir, thrHold))
        sys.stdout.flush()
    elif sys.argv[1] == 'get_objectdetection':
        print(Provider.get_objectdetection())
        sys.stdout.flush()
    elif sys.argv[1] == 'compression':
        videoPath = sys.argv[2]
        videoDir = sys.argv[3]
        widthD = int(sys.argv[4])
        heightD = int(sys.argv[5])
        fps = int(sys.argv[6])
        fileFormat = sys.argv[7]
        print(Provider.compression(videoPath, videoDir,
              widthD, heightD, fps, fileFormat))
        sys.stdout.flush()
    elif sys.argv[1] == 'get_compression':
        print(Provider.get_compression())
        sys.stdout.flush()
    elif sys.argv[1] == 'facedetection':
        videoPath = sys.argv[2]
        minNegi = int(sys.argv[3])
        print(Provider.facedetection(videoPath, minNegi,
                                     ))
        sys.stdout.flush()
    elif sys.argv[1] == 'get_facedetection':
        print(Provider.get_facedetection())
        sys.stdout.flush()
    elif sys.argv[1] == 'motion':
        videoPath = sys.argv[2]
        minNegi = int(sys.argv[3])
        print(Provider.motion(videoPath, minNegi
                              ))
        sys.stdout.flush()
    elif sys.argv[1] == 'get_motion':
        print(Provider.get_motion())
        sys.stdout.flush()
    elif sys.argv[1] == 'saliency':
        frameDir = sys.argv[2]
        print(Provider.saliency(frameDir))
        sys.stdout.flush()
    elif sys.argv[1] == 'get_saliency':
        print(Provider.get_saliency())
        sys.stdout.flush()
