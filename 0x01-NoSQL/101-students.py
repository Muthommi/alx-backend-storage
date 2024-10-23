#!/usr/bin/env python3
"""
Function to return all students sorted by the average score.
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by the average score.
    """
    students = mongo_collection.aggregate([
        {
            "$addFields": {
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ])
    return list(students)
