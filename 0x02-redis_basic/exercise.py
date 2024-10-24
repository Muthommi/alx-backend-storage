#!/usr/bin/env python3
"""
This module defines a Cache class for storing data.
"""


import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator counting how many times a method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapped method that increments the call count each time
        it is called.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores history of inputs and outputs for method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapped method to store input arguments and return values.
        """

        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


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

    @count_calls
    @call_history
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


def replay(method: Callable):
    """
    Displays call history of a particular function.
    """
    redis = method.__self__._redis
    method_name = method.__qualname__
    inputs_key = f"{method_name}:inputs"
    outputs_key = f"{method_name}:outputs"

    inputs = redis.lrange(inputs_key, 0, -1)
    outputs = redis.lrange(outputs_key, 0, -1)

    call_count = len(inputs)
    print(f"{method_name} was called {call_count} times:")

    for inp, out in zip(inputs, outputs):
        print(
            f"{method_name}(*{inp.decode('utf-8')}) -> "
            f"{out.decode('utf-8')}"
        )
