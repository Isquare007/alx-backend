#!/usr/bin/env python3
"""
LFU caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """"
    inherits from BaseCaching
    """

    def __init__(self):
        """
        Initializing MRUCache
        """
        super().__init__()
        self.stack = []
        self.pair = OrderedDict()

    def put(self, key, item):
        """Assign key and item
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.stack:
            least = min(self.pair, key=self.pair.get)
            self.pair.pop(least)
            index = self.stack.index(least)
            discard = self.stack.pop(index)
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

        if key and item:
            if key in self.stack:
                self.stack.remove(key)

            self.stack.append(key)
            self.pair[key] = 1
            self.cache_data[key] = item

    def get(self, key):
        """
        Fetch data with key
        """
        if not key or key not in self.cache_data:
            return None

        if key in self.pair:
            self.pair[key] += 1
        return self.cache_data[key]
