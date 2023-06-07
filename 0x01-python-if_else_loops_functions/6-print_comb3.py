#!/usr/bin/python3
for s in range(10):
    for h in range(s+1, 10):
        print("{:02d}".format(s*10+h), end='')
