import cv2
import sharedvar

class Camera:
    def __init__(self, sharedFrame: sharedvar, cam_index = 0):
        self.shared_frame = sharedFrame
        self.camera_index = cam_index
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            raise Exception ("Could not open webcam...")
        
    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame
    
    
    # Function that writes frame to shared variable
    def write_frame(self):
        ret, frame = self.cap.read()
        if ret:
            self.shared_frame.cv.acquire()
            try:
                self.shared_frame.var = frame
                self.shared_frame.cv.notify()
            finally:
                self.shared_frame.cv.release()
    
    def release(self):
        self.cap.release()

    def run(self):
        while True:
            self.write_frame()