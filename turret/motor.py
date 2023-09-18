import RPi.GPIO as GPIO
from time import sleep

COUNTERCLOCKWISE = CCW = 1
CLOCKWISE = CW = 0

class motor:
    def __init__(self, pull_pin: int, direction_pin: int, frequency: int) -> None:
        self.__pull_pin = pull_pin
        self.__direction_pin = direction_pin
        self.__period = 1/frequency
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__pull_pin, GPIO.OUT)
        GPIO.setup(self.__direction_pin, GPIO.OUT)
      
    def drive(self, steps:int, direction: bool = True):
        GPIO.output(self.__direction_pin, direction)
        for step in range(steps):
            GPIO.output(self.__pull_pin, GPIO.HIGH)
            sleep(self.__period/2)# Sleep for 5ms
            GPIO.output(self.__pull_pin, GPIO.LOW)
            sleep(self.__period/2)# Sleep for 5ms

        
    