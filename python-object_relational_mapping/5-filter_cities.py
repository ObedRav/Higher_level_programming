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
    state_name = argv[4].split(';')[0].strip("'")

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name,
        charset="utf8")

    cur = conn.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(f"""
    SELECT cities.name
    FROM cities
    INNER JOIN states
    ON cities.state_id = states.id
    WHERE states.name = '{state_name}';
    """)

    query_rows = str(cur.fetchall())
    query_rows = query_rows.replace("{'name': ", "").replace('}', '').replace('(', '[').replace(')', ']')
    print(query_rows)
    cur.close()
    conn.close()


if __name__ == '__main__':
    solution()
