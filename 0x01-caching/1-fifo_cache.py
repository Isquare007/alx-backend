#!/usr/bin/env python3
"""FIFIO Cache Module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO"""
    def __init__(self) -> None:
        """initialize"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache with FIFO algorithm
        """
        if item and key:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = next(iter(self.cache_data.keys()))
                self.cache_data.pop(discard)
                print("DISCARD: {}".format(discard[0]))

    def get(self, key):
        """get value of key passed"""
        return self.cache_data.get(key)
