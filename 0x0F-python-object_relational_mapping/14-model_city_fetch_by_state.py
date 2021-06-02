#!/usr/bin/python3
""" 14-model_city_fetch_by_state """
from model_state import Base, State
from model_city import City
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
    res = session.query(City).join(State).all()
    for row in res:
        print("{}: ({}) {}".format(row.state.name, row.id, row.name))

if __name__ == "__main__":
    get_states()
