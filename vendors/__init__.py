'''creates an instance of class db_storage'''
import os

storage_type = 'db'

if storage_type == 'db':
    from vendors.engine.db_storage import  Db_storage
    storage = Db_storage()
    storage.load()
