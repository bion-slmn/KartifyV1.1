#!usr/bin/python3
''' this module define two vendors and the methods to get the
items they sell (the laptop and the desktop'''

from bs4 import BeautifulSoup
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Vendor:
    ''' this is the base model for all vendors'''
    # creating columns for the vendor table
    name = Column(Text)
    price = Column(Text)
    link = Column(Text)
    img_link = Column(Text)
    catergory = Column(String(20))
    vendor = Column(String(20))
    item_id = Column(Integer, autoincrement=True, primary_key=True)

    def __init__(self, **kwargs):
        '''initialises the vendor and its attributes'''
        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dict(self):
        '''return the dictionary of the obj'''
        new_dict = self.__dict__.copy()
        new_dict.pop('_sa_instance_state')
        return new_dict
