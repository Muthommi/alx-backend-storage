#!/usr/bin/env python3
"""
Function that returns the list of school.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))
