#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = set()
    sum = 0
    for i in my_list:
        if i not in unique_list:
            sum += i
            unique_list.add(i)
    return sum
