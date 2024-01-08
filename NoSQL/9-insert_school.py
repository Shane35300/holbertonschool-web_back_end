#!/usr/bin/env python3
"""
This module contains function that inserts a new document in a collection
based on kwargs
"""


from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """
    mongo_collection will be the pymongo collection object
    Returns the new _id
    """
    resultat_insertion = mongo_collection.insert_one(kwargs)
    return resultat_insertion.inserted_id
