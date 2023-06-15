#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdic = {}
    for i in a_dictionary:
        j = (a_dictionary.get(i)) * 2
        newdic.update({i: j})
    return newdic
