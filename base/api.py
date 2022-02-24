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
