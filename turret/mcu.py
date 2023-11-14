import serial
import serial.tools.list_ports
import json
import time

PITCH_MAXIMUM = 4000
PITCH_MINIMUM = -4000
class Microcontroller:
    def __init__(self, baud, signature) -> None:
        available_ports = serial.tools.list_ports.comports()
        self.port = None
        for port in available_ports:
            if signature in port.description:
                self.port = serial.Serial(port.device, baud)
        if self.port is None: raise Exception("Unable to find mcu")
        self.__pitch_steps_from_calibration_point = 0
        #self.port.open()
        
    def check_for_response(self):
        """Checks if microcontroller has responded.
        """
        if self.port.in_waiting:
            line = self.port.readline().rstrip().decode('utf-8')
            return line
        return None
    
    def shoot(self):
        """Function to send message that will make the mcu trigger shooting mechanism.
        Microcontroller should respond with "Fired" or "Cannot fire, in reload state" depending on its state.
        """
        self.port.write(bytes(json.dumps({"T":1}).encode('utf-8')))
        print(f'sending: {json.dumps({"T":1})}')
    def __clamp(self, value, lower, upper):
        return min(max(value, lower), upper)
    def send_position(self, azimuth_steps: int, pitch_steps: int):
        """Send position to microcontroller.

        Args:
            azimuth_steps: steps to write to azimuth motors
            azimuth_direction: direction for azimuth motors.
            pitch_steps: steps to write to pitch motor
            pitch_direction: Direction for the pitch motor to drive in.
        """
        
        azimuth_direction = 1 if azimuth_steps > 0 else 0
        pitch_direction = 1 if pitch_steps > 0 else 0
        print(f"Pitch dir: {pitch_direction}")
        print(f"Azimuth dir: {azimuth_steps}")
        if pitch_direction:
                if self.__pitch_steps_from_calibration_point + pitch_steps > PITCH_MAXIMUM:
                    pitch_steps = PITCH_MAXIMUM - self.__pitch_steps_from_calibration_point
                    self.__pitch_steps_from_calibration_point = PITCH_MAXIMUM
                    print("Max pitch")
                else:
                    self.__pitch_steps_from_calibration_point += pitch_steps
        else:
            if self.__pitch_steps_from_calibration_point + pitch_steps < PITCH_MINIMUM:
                pitch_steps = PITCH_MINIMUM - self.__pitch_steps_from_calibration_point
                print("Minimum pitch")
            else:
                self.__pitch_steps_from_calibration_point += pitch_steps
        print(f"Pitch pos: {self.__pitch_steps_from_calibration_point}")
        msg = {
            "A":
            {
                "S": abs(azimuth_steps),
                "D": azimuth_direction
            },
            "P":
            {
                "S": abs(pitch_steps),
                "D": pitch_direction
            }
        }
        print(f"Sending: {json.dumps(msg)}")
        self.port.write(bytes(json.dumps(msg).encode('utf-8')))

    def calibrate_pitch(self):
        self.__pitch_steps_from_calibration_point = 0
    def home_pitch(self):
        self.send_position(0,self.__pitch_steps_from_calibration_point*(-1))
        ok = False
        timestamp = time.time()
        while(not ok):
            output = self.check_for_response()
            if output:
                print(output)
                if output == "Done":
                    ok = True
            elif (time.time() - timestamp) >= 10:
                print("Unable to confirm position, mcu timed out")
                break
            time.sleep(0.2)
                
