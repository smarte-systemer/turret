import threading
import numpy as np
import time
class SharedVar:
    def __init__(self) -> None:
        self.var = None
        self.cv = threading.Condition()
    
    def empty(self):
        if not self.var:
            return True
    
    def get_var(self):
        with self.cv:
            self.cv.wait()
            return self.var

    def set_var(self, var):
        with self.cv:
            self.var = var
            self.cv.notify_all()

        # self.cv.acquire()
       # self.cv.wait()
       # try:
       #     self.var = var
       #     self.cv.notify()
       # finally:
       #     self.cv.release()
