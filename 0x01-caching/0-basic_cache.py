#!/usr/bin/python3
""" Implmentation of the Basic Cache Class that
inherits from BaseCaching and is a caching system.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Implmentation of the Basic Cache that
    with inheritance from the parent
    """

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data
        the item for the key. If key or item is None, the
        Method does nothing"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Must return the value in self.cache_data linked
        to key"""
        if key is None or not self.cache_data.get(key, None):
            return
        return self.cache_data.get(key)
