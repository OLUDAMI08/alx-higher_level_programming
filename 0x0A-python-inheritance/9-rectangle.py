#!/usr/bin/python3

"""inherit from basegeometry"""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectange(BaseGeometry):
    """class Rectangle that inherits from
    BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = hight
    
    def area(self):
        """return the area of the rectangle"""
        return self.width * self.height

    def __str__(self):
        """return the print() and str() 
        representation"""
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string

