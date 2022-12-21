#!/usr/bin/python3

class Square:
    """A square class"""
    def __init__(self, size):
        """initializing square class
        Args:
            size(int): represent the size of the square defined
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """
        self.__size = size

    @property
    def size(self):
        """retrieve size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(size, size):
            raise TypeError("ize must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area of square"""

        return (self__size * self__self)
