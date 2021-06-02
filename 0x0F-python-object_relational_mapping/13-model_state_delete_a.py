#!/usr/bin/python3
""" 13-model_state_delete_a """
from model_state import Base, State
import sys
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker


def delete_states():
    """ Deletes states with name containing letter a """
    engine = db.create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                              .format(sys.argv[1],
                                      sys.argv[2],
                                      sys.argv[3]
                                      ), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    delete_tables = session.query(State).filter(
        State.name.like("%a%")
    )
    delete_tables.delete(synchronize_session=False)
    session.commit()

if __name__ == "__main__":
    delete_states()
