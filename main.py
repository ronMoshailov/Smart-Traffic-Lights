import numpy as np
import cv2

from ultralytics import YOLO
from yt_dlp import YoutubeDL

import model_runner
from utility import constants, special

def main():

    ## ========== Load Model ========== ##
    model = YOLO("yolov8n.pt")    # load pretrained model
    # model = YOLO("yolov8m.pt")  # load pretrained model
    # model = YOLO("yolov8l.pt")  # load pretrained model
    # lane_coordinates = np.array([[0 ,  0], [0 ,  0], [0 ,  0], [0 ,  0]])
    # model = YOLO(r"C:\Users\ron.MENORAH-RND\PycharmProjects\ITC\runs\detect\yolo8n_trained\weights\best.pt")
    # model = YOLO(r"C:\Users\User\PycharmProjects\Smart-Traffic-Lights\runs\detect\yolo8l_trained5\weights\best.pt") # l + 100 samples

    ## ========== Day 360p ========== ##
    # video = cv2.VideoCapture(constants.DAY_360P_VIDEO_PATH)
    # lane_coordinates = np.array([
    #     [660  ,  390],      # up   - left
    #     [1050 ,  400],      # up   - right
    #     [2100 ,  850],      # down - right
    #     [1450 ,  900]       # down - left
    # ])

    ## ========== Day 720p ========== ##
    # video = cv2.VideoCapture(constants.DAY_720P_VIDEO_PATH)

    ## ========== Night 720p ========== ##
    # video = cv2.VideoCapture(constants.NIGHT_720P_VIDEO_PATH)

    ## ========== Night 1080p ========== ##
    # video = cv2.VideoCapture(constants.NIGHT_1080P_VIDEO_PATH)

    ## ========== Night #01 Junction ========== ##
    # video = cv2.VideoCapture(constants.NIGHT_01_VIDEO_PATH)

    ## ========== Day Snow ========== ##
    # video = cv2.VideoCapture(constants.DAY_SNOW_720P_VIDEO_PATH)

    ## ========== Day Low Quality ========== ##
    # video = cv2.VideoCapture(constants.DAY_LOW_QUALITY_VIDEO_PATH)

    ## ========== Test ========== ##
    video = cv2.VideoCapture(constants.TEST_NIGHT_VIDEO_PATH)

    ## ========== Webcam ========== ##
    # video = cv2.VideoCapture(0)                                     # use with webcam

    ## ========== Youtube ========== ##
    youtube_url = "https://www.youtube.com/watch?v=B0YjuKbVZ5w"
    ydl_opts = {'format': 'best'}
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=False)
        video_url = info_dict.get("url", None)
    video = cv2.VideoCapture(video_url)

    ## ========== Run ========== ##
    device = special.set_cuda()
    model.to(device)

    model_runner.run_model(model, video, device, lane_coordinates=None, save_images=False, save_interval=20, frame_rate=0)
    # model_runner.train_model(model, device)

if __name__ == "__main__":
    # חשוב מאוד: חובה ב-Windows
    import multiprocessing
    multiprocessing.freeze_support()
    main()
