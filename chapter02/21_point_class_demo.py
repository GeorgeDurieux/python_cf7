import math

class Point:
    """
    A class representing a point in the space

    Attributes:
        x (float): The x axis coordinate.
        y (float): The y axis coordinate.
    """
    def __init__(self, x: float = 0, y: float = 0):
        """
        Initialize a point

        Args:
            x (float): The x axis coordinate. Defaults to 0.
            y (float): The y axis coordinate. Defaults to 0.
        """
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def distance_to(self, other):
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))
    
    def main(): 
        p1 = Point(10, 20)
        p2 = (30, 40)
        print(f'P1: {p1}')
        print(f'P2: {p2}')
        print(f'Distance: {p1.distance_to(p2)}')

    if __name__ == '__main__':
        main()