#!/usr/bin/env python3
"""
This function inserts a new document in the collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in the collection
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
