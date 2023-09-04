"""
Example code using yolo8n model for detection
"""
from ultralytics import YOLO
import cv2 as cv
import numpy as np


video_feed = cv.VideoCapture(0)
model = YOLO("yolov8n.pt")

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]


def do_nothing():
    pass

def filter_hsv(image, lower_bound: np.array, upper_bound: np.array):
    mask = cv.inRange(image, lower_bound, upper_bound)
    return mask


def get_feed(camera):
    while(1):
        hue_min = cv.getTrackbarPos("Hue Min", "Slider")
        hue_max = cv.getTrackbarPos("Hue Max", "Slider")
        sat_min = cv.getTrackbarPos("Saturation Min", "Slider")
        sat_max = cv.getTrackbarPos("Saturation Max", "Slider")
        val_min = cv.getTrackbarPos("Value Min", "Slider")
        val_max = cv.getTrackbarPos("Value Max", "Slider")
        lower_bound = np.array([hue_min, sat_min, val_min])
        upper_bound = np.array([hue_max, sat_max, val_max])

        ret, frame = camera.read()
        if not ret:
            print("Unable to receive frame. Exiting ...")
            break 
        results = model(frame, stream=True)
        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

                # put box in cam
                cv.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

                # confidence
                confidence = np.ceil((box.conf[0]*100))/100
                print("Confidence --->",confidence)

                # class name
                cls = int(box.cls[0])
                print("Class name -->", classNames[cls])

                # object details
                org = [x1, y1]
                font = cv.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                color = (255, 0, 0)
                thickness = 2

                cv.putText(frame, classNames[cls], org, font, fontScale, color, thickness)

        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break

cv.namedWindow("Slider")
cv.resizeWindow("Slider", 640, 480)
cv.createTrackbar("Hue Min", "Slider", 0, 255, do_nothing)
cv.createTrackbar("Hue Max", "Slider", 0, 255, do_nothing)
cv.createTrackbar("Saturation Min", "Slider", 0, 255, do_nothing)
cv.createTrackbar("Saturation Max", "Slider", 0, 255, do_nothing)
cv.createTrackbar("Value Min", "Slider", 0, 255, do_nothing)
cv.createTrackbar("Value Max", "Slider", 0, 255, do_nothing)


get_feed(video_feed)

video_feed.release()
cv.destroyAllWindows()

