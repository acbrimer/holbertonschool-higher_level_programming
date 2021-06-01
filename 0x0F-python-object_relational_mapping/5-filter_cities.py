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
    p_state = ""
    if len(sys.argv) == 5:
        config["user"] = sys.argv[1]
        config["passwd"] = sys.argv[2]
        config["db"] = sys.argv[3]
        p_state = sys.argv[4]
    db = get_connection(**config)
    cursor = db.cursor()
    cursor.execute("""
        SELECT
        c.name
        FROM states AS s
        INNER JOIN cities AS c
            ON s.id = c.state_id
        WHERE s.name COLLATE latin1_general_cs = %s
        ORDER BY c.id;
        """, (p_state,))
    results = cursor.fetchall()
    cities = []
    for row in results:
        cities.append(row[0])
    print(", ".join(cities))

if __name__ == "__main__":
    list_cities()
