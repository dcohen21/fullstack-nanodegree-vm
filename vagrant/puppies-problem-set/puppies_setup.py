#!/usr/bin/env python3

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime
import decimal

Base = declarative_base()


class Shelter(Base):
    __tablename__ = 'shelter'

    name = Column(String(80), nullable=False)
    address = Column(String(250))
    city = Column(String(80))
    state = Column(String(20))
    zipCode = Column(String(10))
    website = Column(String)
    id = Column(Integer, primary_key=True)


class Puppy(Base):
    __tablename__ = 'puppy'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    date_of_birth = Column(Date)
    gender = Column(String(10), nullable=False)
    weight = Column(Numeric)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    picture = Column(String)
    shelter = relationship(Shelter)


engine = create_engine('sqlite:///puppies.db')


Base.metadata.create_all(engine)