#!/usr/bin/python3
"""
a script that changes the name of a State object from the database
"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sys import argv

if __name__ == "__main__":
    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@\
localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    louisstate = State(name="Louisiana")
    session.add(louisstate)
    session.commit()
    print(louisstate.id)
    session.close()
