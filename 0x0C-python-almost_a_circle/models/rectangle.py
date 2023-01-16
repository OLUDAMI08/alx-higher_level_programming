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
        super()__init_(id)_
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

