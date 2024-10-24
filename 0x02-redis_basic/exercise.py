#!/usr/bin/env python3
"""
This module defines a Cache class for storing data.
"""


import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class to interact with Redis storage.
    """
    def __init__(self):
        """
        Initialize the Redis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores given data in Redis with a randomly generated key.
        """
        key = str(uuid.uuid4())

        self._redis.set(key, data)

        return key
