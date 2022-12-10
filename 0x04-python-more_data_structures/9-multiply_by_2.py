#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    dict = {}

    for i in a_dictionary.keys():
        dict.update({i: a_dictionary.get(i) * 2})

    return dict

