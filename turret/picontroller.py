#import motor as Motor
import gui as GUI
import sharedvar as SharedVar
#from turret.sharedvar import SharedVar
import camera as Camera
#import model
#from turret.detector import Detector
import detector as Detector
import threading
import time

class PiController:
    def __init__(self, shared_coord: SharedVar, gui: GUI, camera: Camera) -> None:
        self.shared_coord = shared_coord
        self.gui = gui
        self.camera = camera
        self.model = model
        #self.azimuth_motor = motor()
        #self.pitch_motor = motor()
        #self.trigger_motor = motor()
        
        # Declares threads for start-function
        self.camera_thread = None
        self.gui_thread = None
        self.azimuth_thread = None
        self.pitch_thread = None
        self.model_thread = None

    def start(self):
        self.camera_thread = threading.Thread(target=self.camera.run)
    #    self.gui_thread = threading.Thread(target=self.gui.run)
    #    self.gui_thread.start() 
        self.camera_thread.start()
        time.sleep(2)
#        gui.root.mainloop()
        self.model_thread = threading.Thread(target=self.model.run)
        self.model_thread.start()
        gui.run()

    def calculate_azimuth_steps():
        # Here we read shared_coordinates and use that for calculating azimuth motor-movement

        return

    def calculate_pitch_steps():
        # Here we read shared_coordinates and use that for calculating pitch-movement
        return

    def trigger_fire_motor():
        

        if (gui.isConfirmedTarget and gui.isFire):
            # Call trigger_motor
            # status = somereturnstatus?
            print("Status")
            gui.set_fire(False)

    
    #def run(self):
     #   while True:
            

if __name__ == '__main__':
    shared_frame = SharedVar.SharedVar()
    shared_coordinates = SharedVar.SharedVar()
    gui = GUI.GUI(shared_frame, shared_coordinates)
    camera = Camera.Camera(shared_frame)
    model = Detector.Detector(shared_frame, shared_coordinates)
    pi = PiController(shared_coordinates, gui, camera)
    pi.start()
    #pi_thread = threading.Thread(target=pi.run)
    #pi_thread.start()
    
