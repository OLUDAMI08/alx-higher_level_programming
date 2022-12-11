#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    lst = list(a_dictionary.values())

    if value not in lst:
        return a_dictionary
    else:
        for i in list(a_dictionary.keys()):
            if a_dictionary.get(i) is value:
                del a_dictionary[i]

    return 
