#!/usr/bin/python3
"""
Contains the inherits_from function
"""


def inherits_from(obj, a_class):
    """from the specified class; otherwise False."""
    cls = type(obj)

    """ Base case: Check if the class is exactly the specified class"""
    if cls is a_class:
        return True
    """Recursively check parent classes"""
    for base_class in cls.__bases__:
        if inherits_from(base_class(), a_class):
            return True
    return False
