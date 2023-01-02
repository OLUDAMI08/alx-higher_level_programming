#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """Function that print the first and the last name
    Args:
        first_name:strings character
        last_name:strings character
    Raises:
        TypeError : if first or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("my name is {:s} {:s}".format(first_name, last_name))

        
