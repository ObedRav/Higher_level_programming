#!/usr/bin/python3
"""
Module Name: 4-cities_by_state

Module Description:
This module contains only one function

Module Functions:
- solution() -> None

Module Attributes:
- None
"""
import MySQLdb
from sys import argv


def solution():
    username, password, database_name = argv[1:4]

    with MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name,
            charset="utf8") as conn:

        cur = conn.cursor()
        cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id
        """)

        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

        cur.close()


if __name__ == '__main__':
    solution()
