#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    i = 0
    for j in my_list:
        if j is search:
            new_list[i] = replace
        i += 1
    return new_list
