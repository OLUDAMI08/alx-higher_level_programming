#!/usr/bin/python3

def search_replace(my_list, search, replace):

    new_ls = my_list.copy()

    for i in range(len(my_list)):
        if new_ls[i] == search:
            new_ls[i] = replace

    return new_ls
