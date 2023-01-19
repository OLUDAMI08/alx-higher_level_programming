#!/usr/bin/python3
"""This module contains a square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Defines a format for the string representation of the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """get the value for withd"""
        return self.__width

    @size.setter
    def size(self, value):
        """set the value for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):

        """update attribute of the instance"""
        attributes = ["id", "size", "x", "y"]
        if args and len(args) != 0:
            i = 0
            for arg in args:
                setattr(self, attributes[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return the dictionay representation"""
        return {"id":self.id, "size":self.size, "x":self.x, "y":self.y}
