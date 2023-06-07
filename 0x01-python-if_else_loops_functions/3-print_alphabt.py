#!/usr/bin/python3
for s in range(ord('a'), ord('z')+1):
    if chr(s) not in ('q', 'e'):
        print("{}".format(chr(s)), end='')
