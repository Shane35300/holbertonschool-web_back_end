#!/usr/bin/env python3

from pymongo import MongoClient


def list_all(mongo_collection):
    """ Thisfonction has a collection as argument
    and returns a list of all documents"""
    docs = mongo_collection.find()

    if docs is None:
        return []

    document_list = [doc for doc in docs]

    return document_list
