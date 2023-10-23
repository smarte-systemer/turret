import tkinter as tk
from PIL import Image, ImageTk
import cv2
from turret.sharedvar import SharedVar





class GUI:
    def __init__(self, sharedFrame: SharedVar, sharedCoor: SharedVar):
        self.shared_frame = sharedFrame
        self.shared_coor = sharedCoor

        self.isAutoaim = False
        self.isConfirmedTarget = False
        self.isFire = False

        self.root = tk.Tk()
        self.root.title("Webcam Controller")
        self.camera_label = tk.Label(self.root)
        self.camera_label.pack(side="right", padx=10, pady=10)


        # Create a frame for the d-pad buttons
        d_pad_frame = tk.Frame(self.root)
        d_pad_frame.pack(side="left", padx=10, pady=10)

        # Create the d-pad buttons with custom appearance
        button_size = 4  # Adjust the size as needed

        up_button = tk.Button(d_pad_frame, text="▲", font=("Helvetica", 24), width=button_size, height=button_size)
        down_button = tk.Button(d_pad_frame, text="▼", font=("Helvetica", 24), width=button_size, height=button_size)
        left_button = tk.Button(d_pad_frame, text="◄", font=("Helvetica", 24), width=button_size, height=button_size, command=tk.LEFT)
        right_button = tk.Button(d_pad_frame, text="►", font=("Helvetica", 24), width=button_size, height=button_size, command=tk.RIGHT)

        up_button.grid(row=0, column=1)
        down_button.grid(row=2, column=1)
        left_button.grid(row=1, column=0)
        right_button.grid(row=1, column=2)

        # Create buttons for autoaim, confirm target, and fire
        autoaim_button = tk.Button(self.root, text="Toggle Autoaim", command=self.toggle_autoaim)
        confirm_target_button = tk.Button(self.root, text="Confirm Target", command=self.toggle_confirm_target)
        fire_button = tk.Button(self.root, text="Fire", command=self.call_fire)

        autoaim_button.pack(side="bottom", padx=10, pady=10)
        confirm_target_button.pack(side="bottom", padx=10, pady=10)
        fire_button.pack(side="bottom", padx=10, pady=10)


    def toggle_autoaim(self):
        self.isAutoaim = not self.isAutoaim
        if self.isAutoaim:
            print("Autoaim: ON")
        else:
            print("Autoaim: OFF")
        

    def toggle_confirm_target(self):
        self.isConfirmedTarget = not self.isConfirmedTarget
        if self.isConfirmedTarget:
            print("Target CONFIRMED")
        else:
            print("Target NOT CONFIRMED")

    def call_fire(self):
        self.isFire = True
        print("FIRING")

    def set_fire(self, val: bool):
        self.isFire = val

    def update_camera_feed(self):

        self.shared_frame.cv.acquire()
        frame = self.shared_frame.var
        self.shared_frame.cv.release()

        if frame is not None:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # I think this works when checking for the coordinates and draw rectangles?
            if not self.shared_coor.empty():
                
                # Acquires the coordinates
                self.shared_coor.cv.acquire()
                x1, y1, x2, y2 = self.shared_coor.var #Stores coordinates in four variables
                # object_id = self.shared_coor.var.second?
                self.shared_coor.cv.release()

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                cv2.putText(frame, "object_ID", (x1 + 10, y1 + 10), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
            image = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image=image)
            self.camera_label.config(image=photo)
            self.camera_label.photo = photo
            self.camera_label.after(10, self.update_camera_feed)  # Update every 10 milliseconds
    
    def run(self):
        self.root.after(10, self.update_camera_feed)