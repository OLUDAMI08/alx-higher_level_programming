#!/usr/bin/python3
""" A m function that read a text file stdout"""


def read_file(filename=""):
    """A function that accept an argument

    Args:
        filename: the file that is passed
        as an argument"""
        with open(filename, 'r', encoding="utf-8") as f:
            print(f.read(), end="")

