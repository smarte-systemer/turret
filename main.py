from turret.communication import Communication
import cv2

ci = Communication('192.168.1.77')

camera = cv2.VideoCapture(0)

while True:
    value, frame = camera.read()
    if value:
        ci.send_frame(frame)