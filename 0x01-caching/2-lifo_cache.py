#!/usr/bin/env python3
"""LIFO Cache Module"""
BaseCaching = __import__('basic_caching').BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self) -> None:
        """initialize"""
        super().__init__()
        self.keyys = []

    def put(self, key, item):
        """ Add an item in the cache with LIFO algorithm
        """
        if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                and key not in self.keyys:
            discard = self.keyys.pop()
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))
        if key and item:
            self.keyys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data[key]


my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
