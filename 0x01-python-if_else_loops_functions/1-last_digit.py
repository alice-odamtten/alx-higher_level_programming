#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastnumber = number % 10
else:
    lastnumber = number % -10
str1 = "Last digit of %d is %d" % (number, lastnumber)
if lastnumber > 5:
    print(str1, "and is greater than 5")
elif lastnumber == 0:
    print(str1, "and is 0")
else:
    print(str1, "and is less than 6 and not 0")
