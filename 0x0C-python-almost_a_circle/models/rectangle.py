#!/usr/bin/python3
"""A Rectangle class that inherit from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherit from base

    Attribute:
    witdth(int): width of the rectangle
    height(int): height of the rectangle
    x: x axis
    y: y axis
    id(int or none): id of the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiation"""
        super()__init_(id)_
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ rectangle width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """rectangle width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """rectangle height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """rectangle height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x axis"""
        return self.__x

    @x.setter
    def x(self, x_axis):
        """y axis setter"""
        if type(x_axis) is not int:
            raise TypeError("x of the attribute> must be an integer")
        if x_axis < 0:
            raise ValueError("x must be > 0")
        self.__x = x_axis

    @property
    def y(self):
        """y axis getter"""
        return self.__y

    @y.setter
    def y(self, y_axis):
        """ y axis setter"""
        if type(y_axis) is not int:
            raise TypeError("y of the attribute> must be an integer")
        if y_axis < 0:
            raise ValueError("y must be > 0")
        self.__y = y_axis

    def area(self):
        """area of the rectangle"""
        return self__height * self__weight

    def display(self):
