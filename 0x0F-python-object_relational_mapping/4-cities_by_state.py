#!/usr/bin/python3
""" a script that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """ get the command line argument and Connect to the MySQL server
    running on localhost at port 3306"""
    db_connect = MySQLdb.connect(host="localhost", port=3306,
                                 user=sys.argv[1], passwd=sys.argv[2],
                                 db=sys.argv[3])
    """ Prepare a cursor object"""
    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT cities.id, cities.name, states.name \
                        FROM cities JOIN states ON cities.state_id \
                        = states.id ORDER BY cities.id ASC")
    datas_fetched = db_cursor.fetchall()
    for data in datas_fetched:
        print(data)

    """Close cursor and database connection"""
    db_cursor.close()
    db_connect.close()
