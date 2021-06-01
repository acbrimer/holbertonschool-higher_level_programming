#!/usr/bin/python3
""" 8-model_state_fetch_first """
from model_state import Base, State
import sys
import sqlalchemy as db


def fetch_all():
    """ Fetches all rows from State """
    engine = db.create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                              .format(sys.argv[1],
                                      sys.argv[2],
                                      sys.argv[3]
                                      ), pool_pre_ping=True)
    with engine.connect() as conn:
        stmt = db.select([State.id, State.name]).limit(1)
        results = conn.execute(stmt)
        if not results:
            print("Nothing")
        else:
            for row in results:
                print("{}: {}".format(row[0], row[1]))

if __name__ == "__main__":
    fetch_all()