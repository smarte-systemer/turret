import pandas

class Interpolation:
    def __init__(self, calibration_file: str, x_column: str, y_column: str) -> None:
        dataframe = pandas.read_csv(calibration_file)
        self.__x_values = dataframe[x_column]
        self.__y_values = dataframe[y_column]

    def linear_interpolation(self, x: float)-> float:
        """Calculates linear interpolation for y given x

        Args:
            x: x-value

        Returns:
            Returns interpolated y-value
        """
        for i in range(len(self.__x_values)):
            if self.__x_values[i] <= x and self.__x_values[i+1] >= x:
                return self.__y_values[i] + (self.__y_values[i+1] - self.__y_values[i])*(x-self.__x_values[i])/(self.__x_values[i+1] - self.__x_values[i])
            
    
   
    def __polynomial_coefficients(self, x: float)->list:
        """Calculates polynomial coefficients

        Args:
            x: value

        Returns:
            list for coefficients
        """
        n = len(self.__x_values)
        coefficients = [0]*n
        for i in range(n):
            coefficient = 1
            for j in range(n):
                if i != j:
                    coefficient *= ((x - self.__x_values[j])/(self.__x_values[i] - self.__x_values[j]))
            coefficients[i] = coefficient
        return coefficients 

    def polynomial_interpolation(self, x: float)->float:
        """Calculates interpolation polynomial

        Args:
            x: value

        Returns:
            Interpolated y-value
        """
        coefficients = self.__polynomial_coefficients(x)
        return sum([coefficients[i]*self.__y_values[i] for i in range(len(self.__x_values))])