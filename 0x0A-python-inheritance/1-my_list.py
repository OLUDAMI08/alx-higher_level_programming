#!/usr/bin/python3

"""This module inherit from the list class"""

class MyList(list):
    """A class that inherit from list"""
    def print_sorted(self):
        """A method to print a sorted list"""
        print(sorted(self))
