import provider as Provider
import sys
import database.db as DB
import cv2


if __name__ == '__main__':
    if sys.argv[1] == 'init':
        print(cv2.__file__)
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
    # elif sys.argv[1] == 'shot_bundry_detection':
    #     videoPath = sys.argv[2]
    #     videoFileName = sys.argv[3]
    #     method = sys.argv[4]
    #     treshold = sys.argv[5]
    #     print(Provider.fe_shot_boundry_det(
    #         videoPath, videoFileName, method, treshold))
    #     sys.stdout.flush()
    elif sys.argv[1] == 'manual_frame':
        videoPath = sys.argv[2]
        videoFileName = sys.argv[3]
        time = sys.argv[4]
        print(Provider.fe_manual_frame(videoPath, videoFileName, time))
        sys.stdout.flush()
