import cv2
import os


class ExtractFrames():
    def __init__(self):
        self.videopath = "/home/pi/videos/video1.h264"

    def extract_frames(self):

        # Read the video from specified path
        cam = cv2.VideoCapture(self.videopath)
        ret, frame = cam.read()
        if ret:
            image_name = "/home/pi/videos/image_1.jpg"
            cv2.imwrite(image_name, frame)
        cam.release()
        cv2.destroyAllWindows()
        return()

    
if __name__== "__main__":
    my_frames = ExtractFrames()
    my_frames.extract_frames()
  