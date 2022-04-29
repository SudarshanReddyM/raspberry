from picamera import PiCamera
import time


class Frames():
    def __init__(self):
        self.time_to_execute = 10

    def record_video(self):
        camera = PiCamera()
        time.sleep(2)
        camera.resolution = (1280, 720)
        camera.vflip = True
        camera.contrast = 10
        executed_time = 0
        video_number = 1
        while executed_time < self.time_to_execute:
            file_name = "/home/pi/videos/" + "video" + str(video_number) + ".h264"
            print("Start recording...")
            camera.start_recording(file_name)
            camera.wait_recording(0.5)
            camera.stop_recording()
            print("Done.")
            executed_time += 0.5
            video_number += 1

if __name__ == "__main__":
    my_frames = Frames()
    my_frames.record_video()

