import tkinter as tk
from PIL import Image, ImageTk
import multiprocessing
from turret.motor import Motor
import cv2
from tflite_support.task import core, processor, vision


#THESE SHOULD  BE ORGANIZED IN SEPARATE FILES. I ONLY USE ONE FILE ATM

#The shared_queue_semaphore should be passed as parameter to constructors
#shared_queue_semaphore = multiprocessing.Semaphore()

class CameraFeed:
    def __init__(self, cam_index = 0):
        self.camera_index = cam_index
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            raise Exception ("Could not open webcam...")
        
    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame
    
    def release(self):
        self.cap.release()


class GUI:
    def __init__(self, camera_feed, shared_queue, shared_queue_semaphore):
        self.camera_feed = camera_feed
        self.shared_queue = shared_queue
        self.shared_queue_semaphore = shared_queue_semaphore
        self.root = tk.Tk()
        self.root.title("Webcam Controller")
        self.camera_label = tk.label(self.root)
        self.camera_label.pack(side="right", padx=10, pady=10)


        # Create a frame for the d-pad buttons
        d_pad_frame = tk.Frame(self.root)
        d_pad_frame.pack(side="left", padx=10, pady=10)

        # Create the d-pad buttons with custom appearance
        button_size = 4  # Adjust the size as needed

        up_button = tk.Button(d_pad_frame, text="▲", font=("Helvetica", 24), width=button_size, height=button_size)
        down_button = tk.Button(d_pad_frame, text="▼", font=("Helvetica", 24), width=button_size, height=button_size)
        left_button = tk.Button(d_pad_frame, text="◄", font=("Helvetica", 24), width=button_size, height=button_size, command=self.left)
        right_button = tk.Button(d_pad_frame, text="►", font=("Helvetica", 24), width=button_size, height=button_size, command=self.right)

        up_button.grid(row=0, column=1)
        down_button.grid(row=2, column=1)
        left_button.grid(row=1, column=0)
        right_button.grid(row=1, column=2)

        # Create buttons for autoaim, confirm target, and fire
        autoaim_button = tk.Button(self.root, text="Toggle Autoaim", command=self.toggle_autoaim)
        confirm_target_button = tk.Button(self.root, text="Confirm Target", command=self.confirm_target)
        fire_button = tk.Button(self.root, text="Fire", command=self.fire)

        autoaim_button.pack(side="bottom", padx=10, pady=10)
        confirm_target_button.pack(side="bottom", padx=10, pady=10)
        fire_button.pack(side="bottom", padx=10, pady=10)

    def toggle_autoaim(self):
        # Add your autoaim logic here
        print("Toggle Autoaim")

    def confirm_target(self):
        # Add your confirm target logic here
        print("Confirm target")

    def fire(self):
        # Add your fire logic here
        print("Fire!!!!!!")

    def update_camera_feed(self):
        frame = self.camera_feed.get_frame()
        if frame is not None:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # I think this works when checking for the coordinates and draw rectangles?
            if not self.shared_queue.empty():
                self.shared_queue_semaphore.acquire() 
                x1, y1, x2, y2 = self.shared_queue.get()
                self.shared_queue_semaphore.release()
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                cv2.putText(frame, self.text, (x1 + 10, y1 + 10), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
            image = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image=image)
            self.camera_label.config(image=photo)
            self.camera_label.photo = photo
        self.camera_label.after(10, self.update_camera_feed)  # Update every 10 milliseconds

    def run(self):
        self.update_camera_feed()
        self.root.mainloop()



# HERE WE NEED A CLASS FOR THE OBJECT DETECTION-MODEL. 
# IT SHOULD HAVE SHARED_QUEUE AND SHARED_QUEUE_SEMAPHORE AS A PARAMETER FOR CREATING THE OBJECT
# THE OBJECT SHOULD HAVE A METHOD LIKE DETECT_OBJECT_FROM_FRAME OR SOMETHING
# WHICH PUTS THE OBJECT COORDIATES TO THE shared_queue THAT CAN BE READ BY GUI AND BY MOTOR

def main():
    shared_queue = multiprocessing.Queue()
    shared_queue_semaphore = multiprocessing.Semaphore()
    
    camera_feed = CameraFeed()
    gui = GUI(camera_feed, shared_queue, shared_queue_semaphore)
    detectionmodel = DetectionModel(camera_feed, shared_queue, shared_queue_semaphore)
    
    ## The Motor should also have shared_queue as parameter in constructor. We need to implement a run-function as well which such as gui and detectionmodel
    azimuthmotor = Motor()
    
    azimuthmotor.run()
    detectionmodel.run()
    gui.run()

if __name__ == '__main__':
    main()


