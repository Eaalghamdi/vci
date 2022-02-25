# import cv2
# import glob
# import pandas


# class FaceDetection:

#     def findFacesStatic(self, frames):
#         """ Args 
#         frames = list of frames 
#         """

#         cols = ['frame', 'Number_of_Faces']
#         results = []

#         face_cascade = cv2.CascadeClassifier(
#             "FeatureExtraction/src/haarcascade_frontalface_default.xml")
#         for frame in frames:
#             img = cv2.imread(frame)
#             # convert to grayscale
#             gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             faces = face_cascade.detectMultiScale(
#                 gray_img, scaleFactor=1.05, minNeighbors=5)

#             for x, y, w, h in faces:
#                 img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
#             resised = cv2.resize(img, (int(img.shape[1]), (int(img.shape[0]))))
#             numberFaces = len(faces)

#         # add features to results
#             results.append([frame, numberFaces])
#         df = pandas.DataFrame(results, columns=cols)
#         df.to_csv("Face_Detection_Static_Results.csv")

#     def findFacesMotion(self, video):
#         pass


# ### Debuging ###
# # imgs = [img for img in glob.glob("test_imgs/*.jpg")]
# # g = FaceDetection()
# # g.findFacesStatic(imgs)
