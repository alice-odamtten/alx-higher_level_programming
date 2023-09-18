#!/usr/bin/python3
"""
a script that lists all states with a name starting with N from the database
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = argv[3]
    connectionn = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=db, port=3306
    )
    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name like 'N%' ORDER BY states.id ASC"
            )
    result = cursor.fetchall()
    for i in result:
        print(i)
    cursor.close()
    connectionn.close()
