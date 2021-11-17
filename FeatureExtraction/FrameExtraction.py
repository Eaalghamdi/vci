import cv2


class FrameExtraxtion:
    def extractFrames(self, time):
        count = 0
        success = True
        while success:
            success, image = self.vidcap.read()
            if count % (time*self.fps) == 0:
                cv2.imwrite('%d.jpg' % count, image)
            count += 1
