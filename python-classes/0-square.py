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
    
    @property
    def dict(self):
        """Return dictionary for the square."""
        return {'size': self.__size}