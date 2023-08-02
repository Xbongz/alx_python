#!/usr/bin/python3

"""
The class representing the square.
"""
class Square:
   
    """"
    To initialise the created square instance.
    """
    def __init__(self, size):
       
        self.__size = size # Assign private instance attribute

    """
    define string function
    """
    def __str__(self):
        """
        return string from the square
        """
        return "<class '{}'>\n{{'_{}__size': {}}}".format(self.__class__.__name__, self.__size)

square = Square
print(square)