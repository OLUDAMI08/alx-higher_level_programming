#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db_connect = MySQLdb.connect(host="localhost", port=3306,
                                 user=username, passwd=password, db=db_name)
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states ORDER BY states.id")
    datas_fetched = db_cursor.fetchall()
    for data in datas_fetched:
        print(data)

    db_cursor.close()
    db_connect.close()
