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

    def __str__(self):
        """Return string for square."""
        return f"square({self.__size})"
    
    def area(self):
        """Return area of square"""
        return self.__size ** 2
    
    def dict(self):
        """Return square dictionary"""
        return {'size': self.__size}
        
mysquare = Square(3)
print(type(mysquare))
print(mysquare.dict())

mysquare = Square(89)
print(type(mysquare))
print(mysquare.dict())

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(mysquare._size)
except Exception as e:
    print(e)
