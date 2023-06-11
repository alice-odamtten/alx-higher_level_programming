#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = tuple_a + (0, 0)
    j = tuple_b + (0, 0)
    return (i[0] + j[0], i[1] + j[1])
