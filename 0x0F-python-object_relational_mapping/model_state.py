#!/usr/bin/python3

"""This script defines a State class and an instance"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State class represents a state table in a MySQL database. """
    __tablename__ = "state"
    
    """table column"""
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
