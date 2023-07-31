#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size

square = Square(3)
print(type(square))
print(square.__dict__)
print(square._Square__size)