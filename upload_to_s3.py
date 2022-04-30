import json
import boto3
import io
import time
import argparse

class UploadVideo():
    def __init__(self):
        self.aws_region = "us-east-one"
        self.s3_input_bucket_name = "cse546group27inputvideobucket"
        self.video_path = "/home/pi/videos/"
    
    def video_upload(self, total_number = 600):
        boto3_session = boto3.Session()
        s3 = boto3_session.client("s3")
        number = 1
        time.sleep(3)
        while number <= total_number:
            file_name = "video" + str(number) + ".h264"
            path_of_video_file = self.video_path + file_name
            self.upload_video_to_s3(s3, path_of_video_file, file_name)
            print("upload success")
            number += 1
            time.sleep(0.5)
        return

    def upload_video_to_s3(self, s3_client, file, file_name):
        # s3_client.upload_fileobj(file, self.s3_input_bucket_name, str(file_name))
        # with open(file) as f:
        files = io.open(file, "rb", buffering = 0)
        s3_client.upload_fileobj(io.BytesIO(files.read()), self.s3_input_bucket_name, file_name)
        print("Video uploaded to S3")
        return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", help = "Denotes number of videos will be taken")
    args= parser.parse_args()
    print("Argument number received: ", args.number)
    my_upload  = UploadVideo()
    my_upload.video_upload(total_number=int(args.number))