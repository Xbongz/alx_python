#!/usr/bin/python3
class Square:
    """The class representing the square.

    Attributes:
        __size (int): parameters of the square size.
    """

    def __init__(self, size):
        """"To initialise the created square instance.

        Args:
            size (int): square size.
        """
        self.__size = size
    
    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
    
    def perimeter(self):
        """Return peremeter of the square."""
        return self.__size * 4