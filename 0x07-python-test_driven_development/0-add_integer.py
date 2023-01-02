#!/usr/bin/python3

def add_integer(a, b=98):
    """function that add two integers

    Args:
        a:first integer
        b:second integer
    Return:
        summation of a and b
    Raises:
        TypeError:if either of the argument is not an integer
        or float
    """
    if not isinstance(a,(int,float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a+b
