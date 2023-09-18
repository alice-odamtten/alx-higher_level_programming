#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in the states
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
    sql = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
ORDER BY id".format(argv[4])
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    connectionn.close()
