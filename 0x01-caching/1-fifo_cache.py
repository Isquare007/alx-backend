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
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            keys_list = list(self.cache_data.keys())
            del self.cache_data[keys_list[0]]
            print(f'DISCARD: {keys_list[0]}')

    def get(self, key):
        """get value of key passed"""
        return self.cache_data.get(key)
