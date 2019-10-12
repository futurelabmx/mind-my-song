from pymongo import MongoClient


MONGO_URI = ""


def db_connect(MONGO_URI, db_name, col_name):
    client = MongoClient(MONGO_URI)
    database = client[db_name]
    collection = database[col_name]
    return collection


def db_fetch_all(collection, conditions={}):
    cursor = collection.find(conditions)
    return cursor


def db_fetch_one(collection, conditions={}):
    one = collection.find_one(conditions)
    return one


def db_clean(collection, conditions={}):
    collection.delete_many(conditions)
    return

def db_insert_document(collection, doc):
    return collection.insert_one(doc)
