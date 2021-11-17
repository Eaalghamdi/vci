# import time
# import cv2
# import numpy as np
 
# # initialize the motion saliency object and start the video stream
# saliency = None
# vs = cv2.VideoCapture(0)
# time.sleep(2.0)

# frame_width = int( vs.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height =int( vs.get( cv2.CAP_PROP_FRAME_HEIGHT))

# # loop over frames from the video file stream
# while True:
# 	# grab the frame from the threaded video stream and resize it
# 	# to 500px (to speedup processing)
# 	frame = vs.read()
# 	frame =  np.array(frame).astype(np.uint8)
#     # resizing caues probles try to use already scaled videos (avi in ur video dir)
# # 	frame = imutils.resize(frame, width=500)
# 	frame = cv2.resize(frame, (frame_width, frame_height))
 
# 	# if our saliency object is None, we need to instantiate it
# 	if saliency is None:
# 		saliency = cv2.saliency.MotionSaliencyBinWangApr2014_create()
# 		saliency.setImagesize(frame_width, frame_height)
# 		saliency.init()
        
# 	# convert the input frame to grayscale and compute the saliency
# 	# map based on the motion model
# 	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# 	(success, saliencyMap) = saliency.computeSaliency(gray)
# 	saliencyMap = (saliencyMap * 255).astype("uint8")
 
# 	# display the image to our screen
# 	cv2.imshow("Frame", frame)
# 	cv2.imshow("Map", saliencyMap)
# 	key = cv2.waitKey(1) & 0xFF
 
# 	# if the `q` key was pressed, break from the loop
# 	if key == ord("q"):
# 		break
 
# # do a bit of cleanup
# cv2.destroyAllWindows()
# vs.stop()



# # import the necessary packages
# from imutils.video import VideoStream
# from imutils.video import FileVideoStream
# import imutils
# import time
# import cv2
# import numpy as np
 
# # initialize the motion saliency object and start the video stream
# saliency = None
# # vs = FileVideoStream("GA102.avi").start()
# vs = cv2.VideoCapture("GA102.avi")

# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# # fourcc = cv2.VideoWriter_fourcc('F','M','P','4')
# # fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
# out = cv2.VideoWriter("output.avi", fourcc,30,(int(vs.get(3)),int(vs.get(4))), False)
# # out = cv2.VideoWriter("output.avi", fourcc, 30, (430,320), False)

# # loop over frames from the video file stream
# while True:
# 	# grab the frame from the threaded video stream and resize it
# 	# to 500px (to speedup processing)
# 	# frame = vs.read()
	
# 	# dim = (420, 320)
# 	# frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
# 	ret, frame = vs.read()
# 	if ret == True:
# 		# frame = imutils.resize(frame, width=430)
# 		frame = cv2.resize(frame, (430, 320))

	
# 	# if our saliency object is None, we need to instantiate it
# 	if saliency is None:
# 		saliency = cv2.saliency.MotionSaliencyBinWangApr2014_create()
# 		# saliency.setImagesize(frame.shape[1], frame.shape[0])
# 		saliency.setImagesize(430, 320)
# 		saliency.init()

# 		# convert the input frame to grayscale and compute the saliency
# 		# map based on the motion model
# 		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# 		(success, saliencyMap) = saliency.computeSaliency(gray)
# 		saliencyMap = (saliencyMap * 255).astype("uint8")

# 		# display the image to our screen
# 		# cv2.imshow("Frame", frame)
# 		cv2.imshow("Map", saliencyMap)
# 		out.write(np.uint8(saliencyMap))
		
# 		key = cv2.waitKey(1) & 0xFF
  
# 		# if the `q` key was pressed, break from the loop
# 		if key == ord("q"):
# 			break
	
# # do a bit of cleanup
# vs.release()
# out.release()

# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FileVideoStream
import imutils
import time
import cv2
 
# initialize the motion saliency object and start the video stream
saliency = None
vs = FileVideoStream("GA102.avi").start()

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter("output.avi", fourcc, 5.0, (430,320), 3)

# loop over frames from the video file stream
while True:
	# grab the frame from the threaded video stream and resize it
	# to 500px (to speedup processing)
	frame = vs.read()
	if frame is not None:
		# frame = imutils.resize(frame, width=500)
	
		# if our saliency object is None, we need to instantiate it
		if saliency is None:
			saliency = cv2.saliency.MotionSaliencyBinWangApr2014_create()
			saliency.setImagesize(frame.shape[1], frame.shape[0])
			saliency.init()

		# convert the input frame to grayscale and compute the saliency
		# map based on the motion model
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		(success, saliencyMap) = saliency.computeSaliency(gray)
		saliencyMap = (saliencyMap * 255).astype("uint8")

		# when printing how many chaneels it gives 2
		# print(len(saliencyMap.shape))


		threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,
			cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
		# using trheshold map to draw contours and count them
		# contours, h = cv2.findContours(threshMap, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
		
		# cv2.drawContours(saliencyMap, contours, -1, (0, 255, 0), 3)
		cvtFrame = cv2.cvtColor(saliencyMap, cv2.COLOR_GRAY2BGR)
		# when printing how many chaneels it gives 3
		# print(len(cvtFrame.shape))


		# display the image to our screen
		# cv2.imshow("Frame", frame)
		cv2.imshow("Map", saliencyMap)
		# cv2.imshow("tresh", threshMap)
		out.write(cvtFrame)
		
		key = cv2.waitKey(1) & 0xFF
	
		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break
	
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()


# import time
# import cv2
 
# # initialize the motion saliency object and start the video stream
# saliency = None
# vs = cv2.VideoCapture(0)
# time.sleep(2.0)

# # loop over frames from the video file stream
# while True:
# 	# grab the frame from the threaded video stream and resize it
# 	# to 500px (to speedup processing)
# 	frame = vs.read()
#     # resizing caues probles try to use already scaled videos (avi in ur video dir)
# # 	frame = imutils.resize(frame, width=500)
 
# 	# if our saliency object is None, we need to instantiate it
# 	if saliency is None:
# 		saliency = cv2.saliency.MotionSaliencyBinWangApr2014_create()
# 		saliency.setImagesize(frame.shape[1], frame.shape[0])
# 		saliency.init()
        
# 	# convert the input frame to grayscale and compute the saliency
# 	# map based on the motion model
# 	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# 	(success, saliencyMap) = saliency.computeSaliency(gray)
# 	saliencyMap = (saliencyMap * 255).astype("uint8")
 
# 	# display the image to our screen
# 	cv2.imshow("Frame", frame)
# 	cv2.imshow("Map", saliencyMap)
# 	key = cv2.waitKey(1) & 0xFF
 
# 	# if the `q` key was pressed, break from the loop
# 	if key == ord("q"):
# 		break
 
# # do a bit of cleanup
# cv2.destroyAllWindows()
# vs.stop()
