#!/usr/bin/python3
"""This module contains a square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Defines a format for the string representation of the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """getter method"""
        return self.__width

    @size.setter
    def size(self, value):
        """setter method"""
        if type(value) is not int:
            raise TypeError(width must be an integer)
        if value <= 0:
            raise ValueError(width must be > 0)
        self.__width = value
        self.__height = value
