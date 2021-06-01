#!/usr/bin/python3
""" model_state """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):

    """ Model for states table """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, )
    name = Column(String(127), nullable=False, )
