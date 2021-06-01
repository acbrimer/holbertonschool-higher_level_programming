#!/usr/bin/python3
""" 4-cities_by_state """
import MySQLdb
import sys


def get_connection(**config):
    """ Safe connection to db with parameters in config """
    try:
        db = MySQLdb.connect(**config)
        return db
    except Exception as err:
        print("Error connecting")
        print(err)
        print(config)
        return err


def list_cities():
    """ Lists cities from db """
    config = {"host": "localhost", "port": 3306,
              "user": "root", "passwd": "", "db": "mysql"}
    if len(sys.argv) == 4:
        config["user"] = sys.argv[1]
        config["passwd"] = sys.argv[2]
        config["db"] = sys.argv[3]
    db = get_connection(**config)
    cursor = db.cursor()
    cursor.execute("""
        SELECT
        c.id
        , c.name
        , s.name AS state
        FROM states AS s
        INNER JOIN cities AS c
            ON s.id = c.state_id
        ORDER BY c.id;
        """)
    results = cursor.fetchall()
    for row in results:
        print(row)

if __name__ == "__main__":
    list_cities()
