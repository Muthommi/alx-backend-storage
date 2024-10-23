#!/usr/bin/env python3
"""
Function that lists all documents in a collection.
"""


def list_all(mongo_collection):
    """
    Lists documents in a collection.
    """
    return list(mongo_collection.find())