import threading
import numpy as np

class SharedVar:
    def __init__(self) -> None:
        self.var = None
        self.cv = threading.Condition()
    
    def empty(self):
        if not self.var:
            return True
    
    def get_var(self):
        return self.var

    def set_var(self, var):
        self.cv.acquire()
        try:
            self.var = var
            self.cv.notify()
        finally:
            self.cv.release()
