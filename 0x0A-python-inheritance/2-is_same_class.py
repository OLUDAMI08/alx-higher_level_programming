#!/usr/bin/python3
"""A module  that returns True if the object is exactly
an instance of the specified class ; otherwise False."""


def is_same_class(obj, a_class):
    """function that return true if the obj is an instance of a class"""

    return isinstance(obj, a_class)
