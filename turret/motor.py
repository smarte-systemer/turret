import RPi.GPIO as GPIO
from time import sleep
from enum import Enum
from PIDRegulator import PIDRegulator



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
    """
    def __init__(self, pulse_pin: int, direction_pin: int, frequency: int, pid_regulator: PIDRegulator, microstep: str = '200') -> None:
        self.__pulse_pin = pulse_pin
        self.__direction_pin = direction_pin
        self.__period = 1/frequency
        self.__steps_per_revolutions = self.__get_revolutions(microstep)
        self.pid_regulator = pid_regulator
        print(self.__steps_per_revolutions)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__pulse_pin, GPIO.OUT)
        GPIO.setup(self.__direction_pin, GPIO.OUT)
        
    
    def update(self, object_coordinate: int, cam_center: int, tolerance: int):
        """Update function called when object is detected
        
        Args: 
            object_coordinate: Position coordinate for detected object
            cam_center: Coordinate for camera center. Only read once.
            tolerance: Tolerance for wanted target for PID-calculation
        """
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
        self.__period = 1/max(min(frequency, 13*10**3), 1)
         
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
            return 200
        elif microstep == '2/A':
            return 400
        elif microstep == '2/B':
            return 400
        elif microstep == '4':
            return 800
        elif microstep == '8':
            return 1600
        elif microstep == '16':
            return 3200
        elif microstep == '32':
            return 6400





