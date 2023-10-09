

class PIDRegulator:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0
        self.integral = 0
        """Class for PID-regulator for smooth motor-movement.
        
        Args:
            Kp: Proportional constant - Needs to be tested for system
            Ki: Integral constant - Needs to be tested for system
            Kd: Derivative contants - Needs to be tested for system
            
        """

    def calculate(self, setpoint, current_pos):
        """Calculates position based on wanted position and current position

        Args:
            setpoint: Wanted value for position
            current_val: Current value for position
        """
        error = setpoint - current_pos
        
        # Proportional
        P = self.Kp * error
        
        # Integral
        self.integral += error
        I = self.Ki * self.integral
        
        # Derivative
        D = self.Kd * (error - self.prev_error)
        self.prev_error = error
        
        return P + I + D