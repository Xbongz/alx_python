#!/usr/bin/python3
"""The module returns True if the object is an instance of a specified class or False if not."""

def is_same_class(obj, a_class):
    """prototype for the instance, which defines an object and a class."""
    
    if isinstance(obj, a_class):
        """To define if if the obj is exactly a class and return true."""
        
        return True
    
    else:
        """If obj is not a class it must return false."""
        return False