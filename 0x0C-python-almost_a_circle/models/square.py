#!/usr/bin/python3
"""square class that inherit from rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super()__init__(self, size, size, x, y, id)

    def __str___(self):
        """format for string representation"""
        return (f"[Square] {self.id} {self.x}/{self.y} - {self.id}")
