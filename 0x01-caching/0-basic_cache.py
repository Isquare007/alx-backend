#!/usr/bin/env python3
"""BasicCache Module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache that inherits from
    BaseCaching and is a caching system"""

    def put(self, key, item):
        if item and key:
            self.cache_data[key] = item

    def get(self, key):
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data[key]
