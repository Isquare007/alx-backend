#!/usr/bin/env python3
"""MRU Cache Module"""
BaseCaching = __import__('basic_caching').BaseCaching


class MRUCache(BaseCaching):
    def __init__(self) -> None:
        """initialize"""
        super().__init__()
        self.keyys = []

    def put(self, key, item):
        """ Add an item in the cache with LRU algorithm
        """
        if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                and key not in self.keyys:
            discard = self.keyys.pop(3)
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))
        if key and item:
            if key in self.cache_data:
                self.keyys.remove(key)
            self.keyys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        if key not in self.cache_data or key is None:
            return None
        self.keyys.remove(key)
        self.keyys.append(key)
        return self.cache_data[key]


my_cache = MRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
