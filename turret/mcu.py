import serial
import serial.tools.list_ports
import json
class Microcontroller:
    def __init__(self, baud, signature) -> None:
        available_ports = serial.tools.list_ports.comports()
        self.port = None
        for port in available_ports:
            if signature in port.description:
                self.port = serial.Serial(port.device, baud)
        if self.port is None: raise Exception("Unable to find mcu")
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

    def send_position(self, azimuth_steps: int, azimuth_direction: bool, pitch_steps: int, pitch_direction: bool):
        """Send position to microcontroller.

        Args:
            azimuth_steps: steps to write to azimuth motors
            azimuth_direction: direction for azimuth motors.
            pitch_steps: steps to write to pitch motor
            pitch_direction: Direction for the pitch motor to drive in.
        """
        msg = {
            "A":
            {
                "S": azimuth_steps,
                "D": azimuth_direction
            },
            "P":
            {
                "S": pitch_steps,
                "D": pitch_direction
            }
        }
        print(f"Sending: {json.dumps(msg)}")
        self.port.write(bytes(json.dumps(msg).encode('utf-8')))
