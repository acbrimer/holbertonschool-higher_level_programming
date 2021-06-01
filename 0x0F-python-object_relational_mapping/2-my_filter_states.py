#!/usr/bin/python3
""" 2-my_filter_states """
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


def list_states():
    """ Lists states from db """
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
        s.*
        FROM states AS s
        WHERE s.name = '%s'
        ORDER BY s.id;
        """ % p_state)
    results = cursor.fetchall()
    for row in results:
        print(row)

if __name__ == "__main__":
    list_states()
