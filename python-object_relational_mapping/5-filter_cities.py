#!/usr/bin/python3
"""
Module Name: 5-filter_cities

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
    state_name = state_name.split(';')[0].strip("'")

    with MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name,
            charset="utf8") as conn:

        cur = conn.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(f"""
        SELECT cities.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        WHERE states.name = '{state_name}';
        """)

        query_rows = str(cur.fetchall())
        query_rows = query_rows = (query_rows
                                   .replace("{'name': '", "")
                                   .replace("'}", "")
                                   .replace('(', '')
                                   .replace(')', ''))
        print(query_rows)
        cur.close()


if __name__ == '__main__':
    solution()
