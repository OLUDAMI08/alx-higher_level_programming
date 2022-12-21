#!/usr/bin/python3

"""class that define a square"""

class Square:
    """Define a class square"""

    def __init___(self, size=0):

        """initializing a class

    Args:
        size(int) - size of the square
    """

       if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

