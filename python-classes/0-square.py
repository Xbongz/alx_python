#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size

square = Square(3)
print(type(square), '\n', square.__dict__, '\n', square._Square__size)