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
