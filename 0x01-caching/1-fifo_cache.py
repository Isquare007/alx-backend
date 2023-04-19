#!/usr/bin/env python3
"""FIFIO Cache Module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self) -> None:
        """initialize"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache with FIFO algorithm
        """
        if item and key is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = next(iter(self.cache_data.keys()))
                self.cache_data.pop(discard)
                print("DISCARD: {}".format(discard[0]))
        return

    def get(self, key):
        """get value of key passed"""
        return self.cache_data.get(key)


my_cache = FIFOCache()
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
