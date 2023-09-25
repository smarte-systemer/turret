import RPi.GPIO as GPIO
from time import sleep

COUNTERCLOCKWISE = CCW = 1
CLOCKWISE = CW = 0

class motor:
    def __init__(self, pull_pin: int, direction_pin: int, enable_pin: int) -> None:
        self.__pull_pin = pull_pin
        self.__direction_pin = direction_pin
        self.__enable_pin = enable_pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__pull_pin, GPIO.OUT)
        GPIO.setup(self.__direction_pin, GPIO.OUT)
        # GPIO.setup(self.__enable_pin, GPIO.OUT)

    def drive(self, steps:int, direction: bool = True):
        # GPIO.output(self.__enable_pin, GPIO.HIGH)
        GPIO.output(self.__direction_pin, direction)
        for step in range(steps):
            GPIO.output(self.__pull_pin, GPIO.HIGH)
            sleep(5*10**(-3))# Sleep for 5ms
            GPIO.output(self.__pull_pin, GPIO.LOW)
            sleep(5*10**(-3))# Sleep for 5ms


        
    