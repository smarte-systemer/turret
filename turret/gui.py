import tkinter as tk
from PIL import Image, ImageTk
import cv2
#from turret.sharedvar import SharedVar
import sharedvar as SharedVar
from detection import Detection



class GUI:
    def __init__(self, sharedFrame: SharedVar, sharedCoor: SharedVar):
        self.shared_frame = sharedFrame
        self.shared_coor = sharedCoor

        self.isAutoaim = False
        self.isConfirmedTarget = False
        self.isFire = False
        self.isLeftButton = False
        self.isRightButton = False
        self.isUpButton = False
        self.isDownButton = False

        self.calibrate = False
        self.home = False
        self.exit = False

        self.root = tk.Tk()
        self.root.title("Webcam Controller")
        self.camera_label = tk.Label(self.root)
        self.camera_label.pack(side="right", padx=10, pady=10)
        self.state = tk.Label(self.root, text="Manual", bg="green")
        self.state.pack(side=tk.TOP)

        # Create a frame for the d-pad buttons
        d_pad_frame = tk.Frame(self.root)
        d_pad_frame.pack(side="left", padx=10, pady=10)

        # Create the d-pad buttons with custom appearance
        button_size = 4  # Adjust the size as needed

        up_button = tk.Button(d_pad_frame, text="▲", font=("Helvetica", 24), width=button_size, height=button_size, command=self.set_up_button)
        down_button = tk.Button(d_pad_frame, text="▼", font=("Helvetica", 24), width=button_size, height=button_size, command=self.set_down_button)
        left_button = tk.Button(d_pad_frame, text="◄", font=("Helvetica", 24), width=button_size, height=button_size, command=self.set_left_button)
        right_button = tk.Button(d_pad_frame, text="►", font=("Helvetica", 24), width=button_size, height=button_size, command=self.set_right_button)

        up_button.grid(row=0, column=1)
        down_button.grid(row=2, column=1)
        left_button.grid(row=1, column=0)
        right_button.grid(row=1, column=2)

        # Create buttons for autoaim, confirm target, and fire
        autoaim_button = tk.Button(self.root, text="Toggle Autoaim", command=self.toggle_autoaim)
        confirm_target_button = tk.Button(self.root, text="Confirm Target", command=self.toggle_confirm_target)
        fire_button = tk.Button(self.root, text="Fire", command=self.call_fire)
        calibrate_button = tk.Button(self.root, text="Calibrate", command=self.set_calibration)
        home_button = tk.Button(self.root, text="Home", command=self.home)

        autoaim_button.pack(side="bottom", padx=10, pady=10)
        confirm_target_button.pack(side="bottom", padx=10, pady=10)
        fire_button.pack(side="bottom", padx=10, pady=10)
        calibrate_button.pack(side="bottom", padx=10, pady=10)
        home_button.pack(side="bottom", padx=10, pady=10)
        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)

    def toggle_autoaim(self):
        self.isAutoaim = not self.isAutoaim
        if self.isAutoaim:
            self.state.config(text="Autoaim", bg="red")
            print("Autoaim: ON")
        else:
            print("Autoaim: OFF")
            self.state.config(text="Manual", bg="green")

    def toggle_confirm_target(self):
        self.isConfirmedTarget = not self.isConfirmedTarget
        if self.isConfirmedTarget:
            print("Target CONFIRMED")
        else:
            print("Target NOT CONFIRMED")

    def call_fire(self):
        self.isFire = True
        print("FIRING")

    def set_fire(self):
        self.isFire = True

    def set_left_button(self):
        if not self.isAutoaim:
            self.isLeftButton = True
        else:
            print("Toggle Autoaim OFF for manual move")
    def set_calibration(self):
        self.calibrate = True
    def home(self):
        self.home = True
    def set_right_button(self):
        if not self.isAutoaim:
            self.isRightButton = True
        else:
            print("Toggle Autoaim OFF for manual move")

    def set_up_button(self):
        if not self.isAutoaim:
            self.isUpButton = True
        else:
            print("Toggle Autoaim OFF for manual move")

    def set_down_button(self):
        if not self.isAutoaim:
            self.isDownButton = True
        else:
            print("Toggle Autoaim OFF for manual move")


    def visulize_detection(self, coordinate: Detection, frame: cv2.typing.MatLike)->cv2.typing.MatLike:
        bottom_left = coordinate.get_bottom_left().get()
        cv2.rectangle(frame, bottom_left, coordinate.get_top_right().get(), (0, 0, 255), 3)
        cv2.circle(frame, coordinate.get_center().get(), 10, (0,0,255), thickness=1)
        cv2.putText(frame, coordinate.get_name(), (bottom_left[0]+ 10, bottom_left[1] + 10), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
        return frame
    def update_camera_feed(self):
#        print("GUI: Update camera feed")
        #self.shared_frame.cv.acquire()
        #frame = self.shared_frame.var
        #self.shared_frame.cv.release()
        frame = None
        frame = self.shared_frame.get_var()
 #       print("GUI: SharedVar released")
        if frame is not None:
  #          print("GUI: Frame found")
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # I think this works when checking for the coordinates and draw rectangles?
            
            coordinates = self.shared_coor.get_var()
            if len(coordinates):
   #             print("GUI: Coordinates found")
                # Acquires the coordinates
            #    self.shared_coor.cv.acquire()

                # Coordinates is stored in format ((x1, y1, x2, y2), object_type)
                # x1 = coordinate[0][0]
                # y1 = coordinate[0][1]
                # x2 = coordinate[0][2]
                # y2 = coordinate[0][3]
                # object_type = coordinate[0][4]
                #x1, y1, x2, y2 = self.shared_coor.var #Stores coordinates in four variables
                # object_id = self.shared_coor.var.second?
               # self.shared_coor.cv.release()
                #frame = cv2.flip(frame, 1)
                # cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                # cv2.putText(frame, object_type, (x1 + 10, y1 + 10), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
                for coordinate in coordinates:
                    self.visulize_detection(coordinate, frame)
             
            cv2.circle(frame, (int(640/2), int(480/2)), 10, (0,0,255), thickness=1)
            image = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image=image)
            self.camera_label.config(image=photo)
            self.camera_label.photo = photo
            self.camera_label.after(10, self.update_camera_feed)  # Update every 10 milliseconds
    def on_exit(self):
        self.home = True
        self.exit = True
        self.root.destroy()


    def run(self):
        self.update_camera_feed()
#        self.camera_label.after(30, self.update_camera_feed)  # Update every 10 milliseconds
#        self.root.after(30, self.update_camera_feed)
        self.root.mainloop()
