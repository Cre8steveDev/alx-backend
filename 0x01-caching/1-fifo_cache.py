#!/usr/bin/python3
""" Implmentation of the FIFO Cache that inherits
from BaseCaching. If the number of items in self.cache_data
is higher than BaseCachin.MAX_ITEMS
You must discard the first item put in the cache
(FIFO Algorithm)
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Implmentation of the FIFO Cache that
    with inheritance from the parent
    """

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data
        the item for the key. If key or item is None, the
        Method does nothing"""
        if key is None or item is None:
            return

        total_keys = list(self.cache_data.keys())

        if len(total_keys) >= self.MAX_ITEMS:
            current_keys = list(self.cache_data.keys())
            print("DISCARD: {}".format(current_keys[0]))
            del self.cache_data[current_keys[0]]

        self.cache_data[key] = item

    def get(self, key):
        """Must return the value in self.cache_data linked
        to key"""
        if key is None or not self.cache_data.get(key, None):
            return
        return self.cache_data.get(key)
