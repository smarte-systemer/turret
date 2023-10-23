class Coordinate:
    def __init__(self, x,y) -> None:
        self.x = x
        self.y = y
    def __init__(self, coordinate: tuple)->None:
        self.x = coordinate[0]
        self.y = coordinate[1]
    def get(self)->tuple:
        return (self.x, self.y)

class Detection:
    """Class to represent a detection made by the model
    """
    def __init__(self, bottom_left: tuple, top_right: tuple, name: str) -> None:
        self.__bottom_left = Coordinate(bottom_left)
        self.__top_right = Coordinate(top_right)
        self.__name = name
    # def __init__(self, x1: int,y1: int ,x2: int, y2: int, name: str) -> None:
    #     self.__init__((x1, y1) , (x2, y2), name)

    def get_bottom_left(self)->Coordinate:
        """Gets bottom left coordinate of the detection box

        Returns:
            Bottom left coordinate
        """
        return self.__bottom_left
    def get_top_right(self)->Coordinate:
        """Gets top right coordinate of the detection box

        Returns:
            Top right coordinate
        """
        return self.__top_right
    def get_name(self)->str:
        """Gets name of category detection

        Returns:
            Name of category detection as string
        """
        return self.__name
    def get_center(self)->Coordinate:
        """Calculate center point between bottom left and top right

        Returns:
            Coordinate with center point
        """
        x_center = self.__bottom_left.x + self.__top_right.x/2
        y_center = self.__bottom_left.y + self.__top_right.y/2
        return Coordinate(x_center, y_center)

    

