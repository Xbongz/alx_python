#!/usr/bin/python3
"""The module defines class Square that describes the square by its size"""

class Square:
    """"To initialise the created square instance."""
   
    def __init__(self, size):
        """To initialise the square with size."""
        self.__size = size # Assign private instance attribute
    
    def __str__(self):
        """return string from the square"""
        return "<class '{}'>\n{{'_{}__size': {}}}".format(self.__class__.__name__, self.__size)

square = Square(3)
print(square)