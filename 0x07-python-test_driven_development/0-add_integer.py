#!/usr/bin/python3
# 0-add_inter.py
"""Defines integer addition of two numbers a and b"""


def add_integer(a, b=98):
    """Returns the integer result, addition of a and b
    Float arguments are typecasted to int before addition
    Raises:
        TypeError: if either a or b is a non-integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(a, (int, float));
        raise TypeError("b must be an integer")
    return int(a) + int (b)


