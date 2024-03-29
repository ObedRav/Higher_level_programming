#!/usr/bin/python3
"""
Module Name: 0-select_states

Module Description:
This module contains only one function

Module Functions:
- solution() -> None

Module Attributes:
- None
"""
import MySQLdb
from sys import argv


def sol():
    username, password, database_name = argv[1:4]

    with MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name,
            charset="utf8") as conn:

        cur = conn.cursor()
        cur.execute("SELECT id, name FROM states ORDER BY id")

        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

        cur.close()


if __name__ == '__main__':
    sol()
