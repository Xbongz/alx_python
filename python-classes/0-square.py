#!/usr/bin/python3
class Square:
    """The class representing the square.

    Attributes:
        size (int): parameters of the square size.
    """

    def __init__(self, size):
        """"To initialise the created square instance.

        Args:
            size (int): square size.
        """
        self.__size = size
square = Square(3)
print(type(square), '\n', square.__dict__, '\n', square.size)