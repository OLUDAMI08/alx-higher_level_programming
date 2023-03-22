#1/usr/bin/python3

"""
This script defines a State class and an instance Base = declarative_base().
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = "state"
        id = column(integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
        name = column(string(128), nullable=False)
