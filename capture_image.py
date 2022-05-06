from picamera import PiCamera
import time

class Captureimage():
    def __init__(self):
        self.path = "/home/pi/images/sudarshan/"

    def capture_picture(self):
        camera = PiCamera()
        number = 1
        time.sleep(5)
        while number < 21:
            file_name = str(number) + ".jpg"
            camera.start_preview()
            camera.capture(self.path + file_name)
            number += 1
            time.sleep(2)
            camera.stop_preview()

        return
if __name__ == "__main__":
    camera = Captureimage()
    camera.capture_picture()