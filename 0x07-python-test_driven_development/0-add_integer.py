#!/usr/bin/python3
"""
Function that adds 2 integers,
the integers must be integers or floats
and returns the addition of them,
"""


def add_integer(a, b=98):
    """
    Check the conditionals.
    """
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b