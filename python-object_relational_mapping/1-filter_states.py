#!/usr/bin/python3
"""
Module Name: 1-filter_states

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
        SELECT id, name
        FROM states
        WHERE name LIKE 'N%' AND BINARY LEFT(name, 1) = BINARY 'N'
        ORDER BY id
        """)

        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

        cur.close()


if __name__ == '__main__':
    solution()
