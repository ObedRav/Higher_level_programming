#!/usr/bin/python3
"""
Module Name: 0-select_states

Module Description:
This module contains only one function

Module Functions:
- sol() -> None

Module Attributes:
- None
"""
import MySQLdb
from sys import argv


def solution():
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name,
        charset="utf8")

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
    conn.close()


if __name__ == '__main__':
    solution()
