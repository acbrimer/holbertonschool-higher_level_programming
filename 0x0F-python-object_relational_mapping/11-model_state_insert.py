#!/usr/bin/python3
""" 11-model_state_insert """
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
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)

if __name__ == "__main__":
    get_states()
