"""
Example code using opencv to filter pixels based on HSV. 
[HSV](https://en.wikipedia.org/wiki/HSL_and_HSV)
"""
import cv2 as cv
import numpy as np

video_feed = cv.VideoCapture(0)

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
        #Display the resulting frame
        hsv_image = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        mask = filter_hsv(hsv_image, lower_bound, upper_bound)
        image = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow('frame', image)
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

