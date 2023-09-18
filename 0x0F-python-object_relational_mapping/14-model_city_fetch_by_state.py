#!/usr/bin/python3
"""
a Python file similar to model_state.py named model_city.py
that contains the class definition of a City.
"""
import sys
from model_city import Base, City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(City).all()
    for city in result:
        print(city)
