#!/usr/bin/python3
class Square:
    """The class representing the square.
    """

    def __init__(self, size):
        """"To initialise the created square instance.
        """
        self.__size = size # Assign private instance attribute

    def __str__(self):
        """return string from the square"""
        return "<class '{}'>\n{{'_{}__size': {}}}".format(self.__class__.__name__, self.__size)

square = Square
print(square)