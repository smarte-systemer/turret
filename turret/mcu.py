import serial
import serial.tools.list_ports
import json
class Microcontroller:
    def __init__(self, baud) -> None:
        available_ports = serial.tools.list_ports.comports()
        self.port = None
        for port in available_ports:
            if 'FT232R USB UART' in port.description:
                self.port = serial.Serial(port.device, baud)
        if self.port is None: raise Exception("Unable to find mcu")
        #self.port.open()
        

    def check_for_response(self):
        if self.port.in_waiting:
            line = self.port.readline().rstrip().decode('utf-8')
            return line
        return None

    def send(self, azimuth_steps: int, azimuth_direction: bool, pitch_steps: int, pitch_direction: bool):
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
        print(f"Sending: f{json.dumps(msg)}")
        self.port.write(bytes(json.dumps(msg).encode('utf-8')))