from turret.communication import Communication
import cv2

ci = Communication('127.0.0.1')

camera = cv2.VideoCapture(0)

while True:
    value, frame = camera.read()
    if value:
        ci.send_frame(frame)