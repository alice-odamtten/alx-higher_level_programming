#!/usr/bin/python3
"""
a script that lists all states with a name starting with N from the database
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    connectionn = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    cursor = connectionn.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name like 'N%' ORDER BY states.id ASC"
            )
    result = cursor.fetchall()
    for i in result:
        if i[1][0] == 'N':
            print(i)
    cursor.close()
    connectionn.close()
