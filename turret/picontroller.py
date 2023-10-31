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
import detection
import motor
class PiController:
    def __init__(self, shared_coord: SharedVar, gui: GUI, camera: Camera) -> None:
        self.shared_coord = shared_coord
        self.gui = gui
        self.camera = camera
        self.model = model
        self.azimuth_motor = motor.Motor(direction_pin=23, pulse_pin=18, 
                     frequency=200, microstep='32')
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
        self.pi_thread = threading.Thread(target=self.run)
        self.pi_thread.start()
        gui.run()




    def pixel_to_step(self, pixels: int, fov: int, microstep: int):
        # 33.75 Pitch FOV
        # FOV/ horizontal pixels
        deg_per_pixel = fov/pixels
        planet_gear_rotation_per_step = 1.8 / microstep
        sun_gear_rotation = planet_gear_rotation_per_step * 1/8
        return round(deg_per_pixel / sun_gear_rotation)

    def move_to_target(self, tolerance):
        print("Move to target start")
        coordinates = shared_coordinates.get_var()  
        if not len(coordinates):
            print("No detections")
            return
        print(coordinates[0].get_center().get())
        object_coordinates = coordinates[0].get_center().get()[0]
        print(object_coordinates)
        cam_center = self.camera.get_resolution()[0]/2
        resolution = self.camera.get_resolution()
        print(f"resolution{self.camera.get_resolution()}")
        pxl_distance = object_coordinates - cam_center
        print(pxl_distance)
        steps_rev = 6400
        # As long as distance is less than tolerance and microsteps is set to 32.
        while(abs(pxl_distance) > tolerance):
            print(f"pxl_distance{pxl_distance}")
            if (pxl_distance < 0):
                self.azimuth_motor.drive(self.pixel_to_step(resolution[0]*10, 60, self.azimuth_motor.get_microstep()), motor.Direction.COUNTERCLOCKWISE)
    #            #self.drive(1 * 6, Direction.COUNTERCLOCKWISE) # Multiplies by 6 since 6 steps approximately is 1 pixel.
                pxl_distance += 1
            elif (pxl_distance > 0):
                self.azimuth_motor.drive(self.pixel_to_step(resolution[0]*10, 60, self.azimuth_motor.get_microstep()), motor.Direction.CLOCKWISE)
                #self.drive(1 * 6, Direction.CLOCKWISE)  # Multiplies by 6 since 6 steps approximately is 1 pixel.
                #print("clockwise")
                pxl_distance -= 1

    def calculate_azimuth_steps(detection: detection.Detection):
        # Here we read shared_coordinates and use that for calculating azimuth motor-movement
        # 60 FOV
        horizontal_pixels = 1280
        center = horizontal_pixels/2
        detection_coordinate = detection.get_center().get()

        diff = detection_coordinate[0] - center
        if diff < 0:
            # left
            pass
        elif diff > 0: 
            #Right
            pass
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

    
    def run(self):
        time.sleep(4)
        #self.azimuth_motor.drive(2000, 1)

        self.azimuth_motor.drive_pwm(100, 1)
        # while True:
       #    self.move_to_target(50)
       #    time.sleep(2)
           
            

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
    
