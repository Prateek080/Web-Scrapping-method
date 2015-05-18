import pymongo

class Connect():

    def get_db():
        from pymongo import MongoClient
        client = MongoClient('localhost:27017')
        db = client.urls
        return db


