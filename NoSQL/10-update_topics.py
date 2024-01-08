#!/usr/bin/env python3
"""
This module contains function that changes all topics of a
school document based on the name
"""


from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Update all school documents with the given name to have the specified topics
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
