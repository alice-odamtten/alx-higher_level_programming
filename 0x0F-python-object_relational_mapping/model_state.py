#!/usr/bin/python3
"""a python file that contains the class definition of a State
"""
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """Defines the state class"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(128))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.id}: {self.name}'
