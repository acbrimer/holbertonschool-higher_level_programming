#!/usr/bin/python3
""" 9-model_state_filter_a """
from model_state import Base, State
import sys
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker


def get_states():
    """ Fetches top row from states """
    engine = db.create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                              .format(sys.argv[1],
                                      sys.argv[2],
                                      sys.argv[3]
                                      ), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).first()
    if row:
        print("{}: {}".format(row.id, row.name))
    else:
        print("Nothing")

if __name__ == "__main__":
    get_states()
