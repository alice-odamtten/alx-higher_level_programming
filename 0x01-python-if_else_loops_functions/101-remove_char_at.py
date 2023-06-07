#!/usr/bin/python3
def remove_char_at(str, n):
    nstr = ""
    for s in range(len(str)):
         if s != n:
             nstr += str[s]
    return nstr
