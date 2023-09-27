# Enkel stygg GUI til camera-feed fra web-cam med funksjonelle
# knapper i fire/confirm target/toggle autoaim som kaller hver sin 
# print-funksjon
# Bruker Tkinter modul. 

import tkinter as tk
import cv2
from PIL import Image, ImageTk
from turret.motor import Motor,Direction

motor_driver = Motor(direction_pin=23, pulse_pin=18, 
                     frequency=2000, microstep='1')

# Function to update the camera feed
def update_camera_feed():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=image)
        camera_label.config(image=photo)
        camera_label.photo = photo
    camera_label.after(10, update_camera_feed)  # Update every 10 milliseconds

# Function to toggle autoaim
def toggle_autoaim():
    # Add your autoaim logic here
    print("Toggle Autoaim")

# Function to confirm target
def confirm_target():
    # Add your confirm target logic here
    print("Confirm target")

# Function to fire
def fire():
    # Add your fire logic here
    print("Fire!!!!!!")

def left():
    motor_driver.drive_revolution(1)
    print("Left")
def right():
    motor_driver.drive_revolution(1, Direction.CCW)
    print("Right")

def set_frequency(event):
    motor_driver.set_frequency(frequency_slider.get())
    revolution_time_label.setvar(str(motor_driver.get_period()*motor_driver.get__steps_per_revolutions()/8))
    root.update_idletasks()

    # Time for one step * steps per revolution
    print(f'Seconds per round: {revolution_time}')

# Create the main Tkinter window
root = tk.Tk()
root.title("Laptop Webcam Controller")

# Create the camera label
camera_label = tk.Label(root)
camera_label.pack(side="right", padx=10, pady=10)

revolution_time = tk.StringVar()
revolution_time_label = tk.Label(root)
revolution_time_label.pack()

# Create a frame for the d-pad buttons
d_pad_frame = tk.Frame(root)
d_pad_frame.pack(side="left", padx=10, pady=10)

# Create the d-pad buttons with custom appearance
button_size = 4  # Adjust the size as needed

up_button = tk.Button(d_pad_frame, text="▲", font=("Helvetica", 24), width=button_size, height=button_size)
down_button = tk.Button(d_pad_frame, text="▼", font=("Helvetica", 24), width=button_size, height=button_size)
left_button = tk.Button(d_pad_frame, text="◄", font=("Helvetica", 24), width=button_size, height=button_size, command=left)
right_button = tk.Button(d_pad_frame, text="►", font=("Helvetica", 24), width=button_size, height=button_size, command=right)

up_button.grid(row=0, column=1)
down_button.grid(row=2, column=1)
left_button.grid(row=1, column=0)
right_button.grid(row=1, column=2)

# Create buttons for autoaim, confirm target, and fire
autoaim_button = tk.Button(root, text="Toggle Autoaim", command=toggle_autoaim)
confirm_target_button = tk.Button(root, text="Confirm Target", command=confirm_target)
fire_button = tk.Button(root, text="Fire", command=fire)
frequency_slider = tk.Scale(root, from_=1, to=13*10**3, command=set_frequency)
frequency_slider.set('1000')
frequency_slider.pack()
set_frequency(None)


autoaim_button.pack(side="bottom", padx=10, pady=10)
confirm_target_button.pack(side="bottom", padx=10, pady=10)
fire_button.pack(side="bottom", padx=10, pady=10)

# Open the laptop's webcam
cap = cv2.VideoCapture(0)  # 0 corresponds to the default webcam, change if needed

if not cap.isOpened():
    raise Exception("Could not open laptop webcam. Make sure it's connected and available.")

# Start camera feed
update_camera_feed()

# Start the Tkinter main loop
root.mainloop()

# Release the webcam and close OpenCV when the window is closed
cap.release()
cv2.destroyAllWindows()
