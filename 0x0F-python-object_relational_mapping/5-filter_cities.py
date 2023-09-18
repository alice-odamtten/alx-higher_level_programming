#!/usr/bin/python3
"""
a script that takes in the name of a state as
an argument and lists all cities of that state
"""

import MySQLdb
from sys import argv
import re

if __name__ == '__main__':
    """Defines a method to get states"""
    connectionn = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1], passwd=argv[2],
            db=argv[3], charset="utf8"
        )
    cursor = connectionn.cursor()
    pattern = "[!@£$%^&*'\"]"
    result = re.search(pattern, argv[4])
    if result is not None and result.group():
        pass
    else:
        cursor.execute(
            "SELECT c.id, c.name FROM cities c LEFT JOIN states s ON \
            c.state_id = s.id WHERE c.state_id = s.id AND s.name LIKE \
            BINARY '{}' ORDER BY c.id ASC".format(argv[4]).strip("'")
        )
        queryrow = cur.fetchall()
        my_set = []
        for i in queryrow:
            myset.append(i[1])
        print(", ".join(my_set))
    cursor.close()
    connectionn.close()
