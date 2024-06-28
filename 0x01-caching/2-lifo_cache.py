#!/usr/bin/python3
""" Implmentation of the LIFO Cache that inherits
from BaseCaching. If the number of items in self.cache_data
is higher than BaseCachin.MAX_ITEMS
You must discard the LAST item put in the cache
(FIFO Algorithm)
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Implmentation of the LIFO Cache that
    with inheritance from the parent
    """

    def __init__(self):
        """Overloading the parent init function"""
        super().__init__()
        self.order_of_entry = []

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data
        the item for the key. If key or item is None, the
        Method does nothing"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS\
                and key not in self.cache_data:
            print("DISCARD: {}".format(self.order_of_entry[-1]))
            del self.cache_data[self.order_of_entry[-1]]
            del self.order_of_entry[-1]

        if key in self.order_of_entry:
            key_index = self.order_of_entry.index(key)
            del self.order_of_entry[key_index]

        self.cache_data[key] = item
        self.order_of_entry.append(key)

    def get(self, key):
        """Must return the value in self.cache_data linked
        to key"""
        if key is None or not self.cache_data.get(key, None):
            return
        return self.cache_data.get(key)
