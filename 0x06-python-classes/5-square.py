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
        self.size = size

    @property
    def size(self):
        """retrieve size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("ize must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area of square"""

        return (self__size * self__size)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

