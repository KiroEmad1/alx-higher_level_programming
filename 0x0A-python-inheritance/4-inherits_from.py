#!/usr/bin/python3
"""
Contains the inherits_from function
"""


def inherits_from(obj, a_class):
    """sgdbvsdfhsdfdsfdfsb"""
    if type(obj) is a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
