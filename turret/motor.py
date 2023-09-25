import RPi.GPIO as GPIO
from time import sleep
from enum import Enum


class Direction(Enum):
    """Enum for directions

    Args:
        Enum: _description_
    """
    COUNTERCLOCKWISE = CCW = 1
    CLOCKWISE = CW = 0

class motor:
    """ 
    Interface for TB6600 motor drive
        Constructor function will set pins to output with [BCM](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html) configuration.
    """

    def __init__(self, pulse_pin: int, direction_pin: int, frequency: int) -> None:
        """Constructor

        Args:
            pulse_pin: Pin used to pulse
            direction_pin: Pin used to determine direction(True/False).
            frequency: _description_
        """
        self.__pulse_pin = pulse_pin
        self.__direction_pin = direction_pin
        self.__period = 1/frequency
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__pulse_pin, GPIO.OUT)
        GPIO.setup(self.__direction_pin, GPIO.OUT)
      

    def drive(self, steps:int):# direction: Direction = Direction.CLOCKWISE):
        """Drive motor in one direction for a number of steps

        Args:
            steps: Number of steps to rotate
            direction:  Direction to rotate. Defaults to clockwise.
        """
        GPIO.output(self.__direction_pin, direction)
        for step in range(steps):
            GPIO.output(self.__pulse_pin, GPIO.HIGH)
            sleep(self.__period/2)
            GPIO.output(self.__pulse_pin, GPIO.LOW)
            sleep(self.__period/2)