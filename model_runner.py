import os
from collections import deque
import cv2
import numpy as np
import time
from ultralytics import YOLO


def run_model(model, video, lane_coordinates=None, save_images=False, save_interval=10, frame_rate=30):
    # Data
    history = deque(maxlen=30)  # List that holds the last 30 elements. complexity of O(1)
    last_save_time = 0
    frame_counter = 0

    # create folder (if needed)
    if save_images:
        os.makedirs("captured_frames", exist_ok=True)

    while True:
        # read frames
        is_success, frame = video.read()
        if not is_success:
            break

        # try every 'frame_rate' model
        frame_counter += 1
        if frame_counter % frame_rate != 0:
            continue

        frame_copy = frame.copy()
        results = model(frame_copy, conf=0.4, imgsz=960)
        for box in results[0].boxes:
            # box.xyxy   - coordinates of the object (x1, y1, x2, y2), left top + right down
            # box.xywh   - coordinates of the object (x_center, y_center, width, height)
            # box.cls    - number category of the object
            # box.conf   - probability of confidence
            # box.id     - number category of the object

            category_number = int(box.cls[0])
            if model.names[category_number] in ["car", "truck", "bus", "motorbike"]:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame_copy, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=1)

                conf = float(box.conf[0])  # 0.0 - 1.0
                text = f"{int(conf * 100)}%"  # לדוגמה: "87%"

                # מיקום הטקסט מעל הקופסה
                cv2.putText(frame_copy, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

        # annotated = results[0].plot()       # draw boxes, labels and confidence percentages for each object
        # cv2.polylines(annotated, [lane_coordinates], isClosed=True, color=(0, 0, 255), thickness=2)  # draw the area to check


        # car_count = 0
        # for box in results[0].boxes:
        #     cls = int(box.cls[0])                                           # number category
        #     if model.names[cls] in ["car", "truck", "bus", "motorbike"]:
        #         x1, y1, x2, y2 = box.xyxy[0]                                # (x1, y1) -> up left, (x2, y2) -> down right
        #         cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)             # center of the box
        #         # res = cv2.pointPolygonTest(lane_coordinates, (cx, cy), False) >= 0
        #         cv2.rectangle(frame_copy, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=2)
        #         # if res:
        #         #     # res < 0: outside the polygon
        #         #     # res = 0: on the edge of the polygon
        #         #     # res > 0: outside the polygon
        #         #     car_count += 1
        #         #     # cv2.circle(annotated, (cx, cy), 4, (0, 255, 0), -1)

        # # הוסף להיסטוריה
        # history.append(car_count)
        # avg_count = sum(history) / len(history)
        #
        # # exceptional load test
        # threshold = 3
        # if avg_count > threshold:
        #     status_text = f"🚨 Traffic congestion! ({int(avg_count)})"
        #     color = (0, 0, 255)
        # else:
        #     status_text = f"Traffic normal ({int(avg_count)})"
        #     color = (0, 255, 0)
        # cv2.putText(annotated, status_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        #
        # ## שמירת תמונה כל X שניות ##
        # if save_images:
        #     current_time = time.time()
        #     if current_time - last_save_time > save_interval:
        #         filename = f"captured_frames/frame_{int(current_time)}.jpg"
        #         cv2.imwrite(filename, frame)
        #         print(f"[INFO] Saved frame: {filename}")
        #         last_save_time = current_time

        cv2.imshow("Detection", frame_copy)  # open window and show the processed frame
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):  # if 'q' pressed -> stop the loop
            break

        # if key == ord("c"):
        #     filename = f"captured_frames/manual_{int(time.time())}.jpg"
        #     cv2.imwrite(filename, frame)
        #     print(f"[INFO] Saved frame manually: {filename}")

    ## ========== Close ========== ##
    video.release()  # end the video and free memory
    cv2.destroyAllWindows()  # close all the windows of OpenCV

def train_model(model):
    model.train(
        data="dataset.yaml",
        epochs=50,  # run of data 50 times. (recommend to be 50-200)
        imgsz=960,
        batch=8,  # how many data to learn each time
        name="yolo8l_trained"
    )