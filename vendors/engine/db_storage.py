#!/usr/bin/python3
'''
the modules defines a database storage
'''
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from vendors.phonex_vendor import Phonex
from vendors.smartbuy_vendor import Smartbuy
from vendors.vendor import Base
from os import getenv

vendor_class = {'phonex': Phonex, 'smartbuy': Smartbuy}


class Db_storage:
    ''' this define the database to store the class of the
        vendors
    '''
    __session = None
    __engine = None

    def __init__(self):
        '''constructs the engine for storage'''
        PROJECT_USER = getenv('PROJECT_USER')
        PROJECT_PWD = getenv('PROJECT_PWD')
        PROJECT_DB = getenv('PROJECT_PWD')
        self.__engine = create_engine(f'mysql+mysqldb://{PROJECT_USER}:{PROJECT_PWD}@localhost/bion_db')

    def new(self, obj):
        ''' this adds a new object to the database
        parameter
            obj (class object): an object of ony of the vendor class
        '''
        self.__session.add(obj)

    def save(self):
        '''this commits and saves the object to the database
        parameter
        '''
        self.__session.commit()

    def load(self):
        '''create all tables and create a session '''
        Base.metadata.create_all(bind=self.__engine)

        # expire on commit is set to false because the requests are readonly
        # scoped_session is used to ensure each request is independent of others
        # and its important for multi-request environment
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def close(self):
        ''' this closes the session'''
        self.__session.remove()

    def drop(self):
        ''' drop deletes all the content in the tables in the database'''
        for v_class in vendor_class.values():
            self.__session.query(v_class).delete()
            self.__session.commit()

    def all(self, cls=None):
        '''it returns a all items in the database

        parameter
        cls (string): a class of vendor in the database
        '''
        new_dict = {}
        if cls is None:
            for v_class in vendor_class.values():
                all_obj = self.__session.query(v_class).all()
                for obj in all_obj:
                    key = '{}.{}'.format(obj.name, obj.vendor)
                    new_dict[key] = obj.to_dict()
            return new_dict

        elif cls and cls in vendor_class:
            v_class = vendor_class.get(cls)
            all_obj = self.__session.query(v_class).all()
            for obj in all_obj:
                key = '{}.{}'.format(obj.name, obj.vendor)
                new_dict[key] = obj.to_dict()
            return new_dict
        return None

    def items(self, category, cls=None):
        '''this method queries the database, for items of a specific catergory
        e.g it can search for only laptops a from specific vendor

        parameter:
        catergory (string): the catergory of items to be
        searched can be laptop or desktop
        cls (string/optional): if true, it will search itemm of
        the specified class of vendor only
        else it will search for items of the all class of vendors'''
        new_dict = {}
        if cls and cls in vendor_class:
            cls = vendor_class.get(cls)
            all_obj = self.__session.query(cls).filter(
                    cls.catergory == category)
            for obj in all_obj:
                key = '{}.{}'.format(obj.name, obj.vendor)
                new_dict[key] = obj.to_dict()
            return new_dict
        if not cls:
            for v_class in vendor_class.values():

                all_obj = self.__session.query(v_class).filter(
                        v_class.catergory == category).all()
                for obj in all_obj:
                    key = '{}.{}'.format(obj.name, obj.vendor)
                    new_dict[key] = obj.to_dict()
            return new_dict

    def search(self, name, vendor=None):
        '''search for an item by name
        parameter:
        name (string/int) : the name that will be used to search
        vendor (string): name of the vendor class to search in
        '''
        new_dict = {}
        if vendor:
            v_class = vendor_class.get(vendor)
            if v_class:
                all_obj = self.__session.query(v_class).filter(
                        v_class.name.like('%{}%'.format(name))).all()
                for obj in all_obj:
                    key = '{}.{}'.format(obj.name, obj.vendor)
                    new_dict[key] = obj.to_dict()
                return new_dict
            return None
                
        for v_class in vendor_class.values():
            all_obj = self.__session.query(v_class).filter(
                    v_class.name.like('%{}%'.format(name))).all()
            for obj in all_obj:
                key = '{}.{}'.format(obj.name, obj.vendor)
                new_dict[key] = obj.to_dict()
        return new_dict
