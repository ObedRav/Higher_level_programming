#!/usr/bin/python3
"""
Module Name: 2-my_filter_states

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
    username, password, database_name, state_name = argv[1:5]

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
        WHERE name = '{}' AND BINARY name = BINARY '{}'
        ORDER BY id;
        """.format(state_name, state_name))

        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

        cur.close()


if __name__ == '__main__':
    solution()
