#!/usr/bin/env python3
"""This module has a function that returns the list of
school having a specific topic"""

def schools_by_topic(mongo_collection, topic):
    """
    Return a list of school documents that have the specified topic
    """
    schools_with_topic = mongo_collection.find({'topics': topic})
    return list(schools_with_topic)
