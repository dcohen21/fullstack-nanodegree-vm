#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppies_setup import Base, Puppy, Shelter
from sqlalchemy import func
import datetime

engine = create_engine('sqlite:///puppies.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def query_one():
    """Prints a list of all puppies in ascending alphabetical order"""

    puppy_list = session.query(Puppy).order_by(Puppy.name.asc()).all()
    for puppy in puppy_list:
        print(puppy.name)


def query_two():
    """Prints a list of puppies under 6 mo old, youngest first"""

    puppy_list = session.query(Puppy.name, Puppy.dateOfBirth)\
        .filter(Puppy.dateOfBirth >= six_months_ago())\
        .order_by(Puppy.dateOfBirth.desc()).all()

    for puppy in puppy_list:
        print(str(puppy.name) + ": " + str(puppy.dateOfBirth))


def query_three():
    """Prints a list of all puppies by ascending weight"""

    puppy_list = session.query(Puppy.name, Puppy.weight)\
        .order_by(Puppy.weight.asc()).all()

    for puppy in puppy_list:
        print(str(puppy.name) + ": " + str(puppy.weight))


def is_leap_year():
    """Helper method to determine whether or not it's a leap year"""

    today = datetime.date.today()
    current_year = today.timetuple()[0]
    if current_year % 4 == 0:
        if current_year % 100 == 0:
            return current_year % 400 == 0
        return True
    return False


def six_months_ago():
    """Helper function to determine the date 6 months ago"""

    # I chose to implement this solution rather than timedelta to get rid
    # of the leap year problem

    today = datetime.date.today()
    day = today.timetuple()[2]
    month = today.timetuple()[1]
    year = today.timetuple()[0]
    month_diff = month - 6

    if month_diff < 1:
        new_month = 12 + month_diff
        year -= 1
    else:
        new_month = month_diff

    return datetime.date(year, new_month, day)
