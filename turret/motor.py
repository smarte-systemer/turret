import RPi.GPIO as GPIO
from time import sleep
from enum import Enum
#from PIDRegulator import PIDRegulator



class Direction(Enum):
        """Enum for directions
        """
        COUNTERCLOCKWISE = CCW = 1
        CLOCKWISE = CW = 0


class Motor:
    """Constructor for motor driver

    Args:
        pulse_pin: Pin used to pulse
        direction_pin: Pin used to assign direction
        frequency: Frequency to pulse, higher -> faster.
        pid_regulator: PID used for calculating necessary movement
        microstep: Which mirostep setting. Defaults '200' 
"""  #shared_queue, shared_queue_semaphore as parameters in init at a later stage
    def __init__(self, pulse_pin: int, direction_pin: int, frequency: int,  microstep: str = '32') -> None:
        self.__pulse_pin = pulse_pin
        self.__direction_pin = direction_pin
        self.__period = 1/frequency
        self.__steps_per_revolutions = self.__get_revolutions(microstep)
        self.__microstep = microstep
        #self.shared_queue = shared_queue
        #self.shared_queue_semaphore = shared_queue_semaphore
        #self.pid_regulator = pid_regulator
        print(self.__steps_per_revolutions)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__pulse_pin, GPIO.OUT)
        GPIO.setup(self.__direction_pin, GPIO.OUT)

    def get_microstep(self)->int:
        microstep = ''.join(d for d in self.__microstep if d.isdigit())
        return int(microstep)
        
    # This function can be called from where the object_coordinates is send.
    # It is precalculated how many steps a pixel is. (6 steps = 1 pixel on camera with FOV 80 and 1080p)
    # The function is made so it should move the turret from one picture. where object is detected.
    # The function should be implemented so it continuosly gets camera-input and can verify movement.
    def move_to_target(self, object_coordinates, cam_center, tolerance):
        pxl_distance = object_coordinates - cam_center
        print(pxl_distance)
        steps_rev = 6400
        # As long as distance is less than tolerance and microsteps is set to 32.
        while(abs(pxl_distance) > tolerance and steps_rev == self.__steps_per_revolutions):
            if (pxl_distance < 0):
                #print("counter clockwise")
                #self.drive(1 * 6, Direction.COUNTERCLOCKWISE) # Multiplies by 6 since 6 steps approximately is 1 pixel.
                pxl_distance += 1
            elif (pxl_distance > 0):
                #self.drive(1 * 6, Direction.CLOCKWISE)  # Multiplies by 6 since 6 steps approximately is 1 pixel.
                #print("clockwise")
                pxl_distance -= 1

        
    """
    def update(self, object_coordinate: int, cam_center: int, tolerance: int):
        Update function called when object is detected
        
        Args: 
            object_coordinate: Position coordinate for detected object
            cam_center: Coordinate for camera center. Only read once.
            tolerance: Tolerance for wanted target for PID-calculation
        
        current_position = cam_center
        target_position = object_coordinate - current_position
        
        # Tolerance is set in function-call. Tolerance is the distance in pixels from center to accepted range of object
        while(abs(target_position) > tolerance):
            target_position = self.pid_regulator.calculate(target_position, current_position)
            
            # This communicates with mechanical components. The stepper motors needs to be done with the previous movement before they can be called again.
            # The time they take needs to be calculated before called upon again. 

            # Simple test case for checking target_position from pid-regulator. This can be implementet "prettier"
            if abs(target_position) > 300:
                self.set_frequency(300)
            elif abs(target_position) < 50:
                self.set_frequency(50)
            else: self.set_frequency(target_position)
            
            # Test for negative values (rotation to the left or pitch downwards)
            if (target_position < 0): 
                self.drive(1, Direction.COUNTERCLOCKWISE)
            else: self.drive(1)
        
    """  
    def drive(self, steps: int, direction: Direction = Direction.CLOCKWISE):
        """Drive motor in one direction for a number of steps

        Args:
            steps: Number of steps to rotate
            direction:  Direction to rotate. Defaults to Direction.CLOCKWISE.
        """
        GPIO.output(self.__direction_pin, bool(direction))
        for step in range(steps):
            GPIO.output(self.__pulse_pin, GPIO.HIGH)
            sleep(self.__period/2)
            GPIO.output(self.__pulse_pin, GPIO.LOW)
            sleep(self.__period/2)

    def drive_revolution(self, revolutions: int, direction: Direction = Direction.CLOCKWISE):
        """Perform full revolutions

        Args:
            revolutions: Number of revolutions to perform
            direction: Direction to rotate in. Defaults to Direction.CLOCKWISE.
        """
        for revolution in range(revolutions):
             self.drive(self.__steps_per_revolutions, direction)
    def set_frequency(self, frequency: int):
        self.__period = 1/max(min(frequency, 13*10**3), 1) # Hva er dette?
         
    def get_period(self)->int:
         return self.__period
    def get__steps_per_revolutions(self):
        return self.__steps_per_revolutions
    def __get_revolutions (self, microstep: str):
        """Matches microstep setting to steps per revolution

        Args:
            microstep: DIP switch setting

        Returns:
            Number of steps per revolution
        """
        """
        match microstep:
              case '1':
                   return 200
              case '2/A':
                   return 400
              case '2/B':
                   return 400
              case '4':
                   return 800
              case '8':
                   return 1600
              case '16':
                   return 3200
              case '32':
                   return 6400
      """
        if microstep == '1':
            return 200 # Steps per revolution
        elif microstep == '2/A':
            return 400 # Steps per revolution
        elif microstep == '2/B':
            return 400 # Steps per revolution
        elif microstep == '4':
            return 800 # Steps per revolution
        elif microstep == '8':
            return 1600 # Steps per revolution
        elif microstep == '16':
            return 3200 # Steps per revolution
        elif microstep == '32':
            return 6400 # Steps per revolution





