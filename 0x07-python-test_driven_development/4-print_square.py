#!/usr/bin/python3

def print_square(size):
    """ A function that print a square with # character
    
    Args:
        size: size lenght of the square

    Raises:
        TypeError:if size is not aninteger
        ValueError: if size is less than zero
        TypeError: is size is a float
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for x in range(size):
        for x in range(size):
            print("#", end='')
        print()
        
