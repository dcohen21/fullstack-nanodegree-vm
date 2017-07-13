#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppies_setup import Base, Puppy, Shelter
from sqlalchemy import func

engine = create_engine('sqlite:///puppies.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def query_one():
    """Prints a list of all puppies in ascending alphabetical order"""

    puppylist = session.query(Puppy).order_by(Puppy.name.asc()).all()
    for puppy in puppylist:
        print(puppy.name)


def query_two():
    """Prints a list of puppies under 6 mo old, youngest first"""



