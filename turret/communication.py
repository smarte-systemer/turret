import socket
import cv2
import numpy as np
import pickle

class Communication:
    """Class to simplify the communication interface to the image processor
    Will stream video to specified server. 
    """
    def __init__(self, server_address: str, server_port: int = 65000, 
                 max_buffer_size: int = 65500, image_format: str = '.jpg') -> None:
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__server = (server_address, server_port)
        self.__max_buffer_size = max_buffer_size
        self.__image_format = image_format

    
    def send_frame(self, frame: cv2.typing.MatLike)->None:
        """_summary_
        Send individual frames
        Args:
            frame (cv2.typing.MatLike): Frame from video stream

        Raises:
            Exception: Unable to encode frame
        """
        return_value, image_buffer = cv2.imencode(self.__image_format, frame)
        if not return_value: raise Exception('Unable to encode frame')
        image_buffer = image_buffer.tobytes()
        number_of_packets = 1
        if len(image_buffer) > self.__max_buffer_size:
            number_of_packets = int(np.ceil(len(image_buffer)/self.__max_buffer_size))
        
        self.__socket.sendto(pickle.dumps({'packets':number_of_packets}), 
                            self.__server)
        left = 0
        right = self.__max_buffer_size
        for packet_index in range(number_of_packets):
            payload = image_buffer[left:right]
            left = right
            right += self.__max_buffer_size
            self.__socket.sendto(payload, self.__server)    
    def __str__(self)->str:
        return self.__repr__

    def __repr__(self) -> str:
        return f'''
                   Server: {self.__server}
                   Max buffer: {self.__max_buffer_size}
                   '''