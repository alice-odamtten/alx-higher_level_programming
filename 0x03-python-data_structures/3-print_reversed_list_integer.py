#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    if len(my_list) == 0:
        return None
    for i in range(a-1, -1, -1):
        print("{:d}".format(my_list[i]))
