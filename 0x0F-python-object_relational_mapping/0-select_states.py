#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Defines a method to get states"""
    connection = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1], passwd=argv[2],
            db=argv[3]
            )
    sqlfomula = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(sqlfomula)
    myresult = cursor.fetchall()
    for i in myresult:
        print(i)
    cursor.close()
    connection.close()
