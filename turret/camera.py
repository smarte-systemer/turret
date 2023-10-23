import cv2
import time
#from turret.sharedvar import SharedVar
import sharedvar as SharedVar
class Camera:
    def __init__(self, sharedFrame: SharedVar, cam_index = 0):
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
            print("Camera: Frame set")
            self.shared_frame.set_var(frame)
            #self.shared_frame.cv.acquire()
            #cv2.imshow("", self.shared_frame.get_var())
            #self.shared_frame.cv.notify_all()
            #self.shared_frame.cv.release()
        else:
            print("No data in frame")
    def release(self):
        self.cap.release()

    def run(self):
        while True:
            self.write_frame()
            key = cv2.waitKey(27)
            if key == 27:
                break
        self.cap.release()
        cv2.destroyAllWindows()
