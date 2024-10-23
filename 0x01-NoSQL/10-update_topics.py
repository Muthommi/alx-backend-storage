#!/usr/bin/env python3
"""
Function that updates topics for school document
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates topics of school document.
    """
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
    )
