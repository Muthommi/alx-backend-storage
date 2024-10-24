#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache
replay = __import__('exercise').replay

cache = Cache()

# Store some data
s1 = cache.store("foo")
s2 = cache.store("bar")
s3 = cache.store(42)

# Replay the history of calls to cache.store
replay(cache.store)
