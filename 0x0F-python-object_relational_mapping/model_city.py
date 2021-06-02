#!/usr/bin/python3
""" model_city """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import State, Base


class City(Base):

    """ Model for cities table """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, )
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    name = Column(String(127), nullable=False, )
    state = relationship(State, primaryjoin=state_id == State.id)
