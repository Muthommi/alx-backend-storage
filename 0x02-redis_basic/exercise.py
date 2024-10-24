#!/usr/bin/env python3
"""
This module defines a Cache class for storing data.
"""


import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    Cache class to interact with Redis storage.
    """
    def __init__(self):
        """
        Initialize the Redis client and flush existing database data
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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float, None]:
        """
        Retrieves data from Redis and applies a conversion function
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves a string value from Redis
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves an integer value from Redis
        """
        return self.get(key, lambda d: int(d))
