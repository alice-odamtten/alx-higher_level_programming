#!/usr/bin/python3
"""a script that lists all cities from the database"""
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
    cursor.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON states.id = cities.state_id \
    ORDER BY cities.id")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    connectionn.close()
