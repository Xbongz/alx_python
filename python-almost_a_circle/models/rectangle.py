#!/usr/bin/python3
"""Module for class Rectangle that inherits from Base"""

"""To import the base file import the class Base"""
from models.base import Base

"""class module that inherits from Base class"""
class Rectangle(Base):
    """Defined rectangle class that will inherit from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """To initialise the attributs """
        super().__init__(id)
        """super to call and use the logic of the init of the Base class"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
    """To get width instance"""
    @property
    def width(self):
        """To difine width method"""
        return self.__width
    
    """To get height instance"""
    @property
    def height(self):
        """To difine width method"""
        return self.__height
    
    """To get x instance"""
    @property
    def x(self):
        """for defining x method"""
        return self.__x
    
    """To get y instance"""
    @property
    def y(self):
        """To define y method"""
        return self.__y
    
    """To set instance for width"""
    @width.setter
    def width(self, value):
        """To define the width method"""
        self.__width = value 
    
    """To set instance for height"""
    @height.setter
    def height(self, value):
        """To define the height method"""
        self.__height = value
    
    """To set instance for X"""
    @x.setter
    def x(self, value):
        """To define the x method to set"""
        self.__x = value

    """To set instance for Y"""
    @y.setter
    def y(self, value):
        """to define the y method"""
        self.__y = value