#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and lists all
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
    sql = "SELECT name FROM cities WHERE state_id = \
    (SELECT id FROM states WHERE name = %s) ORDER BY id"
    cursor.execute(sql, (argv[4],))
    result = cursor.fetchall()
    uple = ()
    for i in result:
        uple += row
    print(*uple, sep=", ")
    cursor.close()
    connectionn.close()
