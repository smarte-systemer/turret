#import motor as Motor
import gui as GUI
import sharedvar as SharedVar
import camera as Camera
#import model
import threading


class PiController:
    def __init__(self, shared_coord: SharedVar, gui: GUI, camera: Camera) -> None:
        self.shared_coord = shared_coord
        self.gui = gui
        self.camera = camera

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
        self.gui_thread = threading.Thread(target=self.gui.run)
        self.camera_thread.start()
        self.gui_thread.start()
        gui.root.mainloop()
        gui.run()

    def calculate_azimuth_steps():
        return

    def calculate_pitch_steps():
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

    pi = PiController(shared_coordinates, gui, camera)
    pi.start()
    #pi_thread = threading.Thread(target=pi.run)
    #pi_thread.start()
    
