#!/usr/bin/env pyhton3
"""BasicChache clas"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A class that add to a caching system"""
    def put(self, key, item):
        """Add item to a cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache by key."""
        if key in self.cache_data:
            return self.cache_data.get(key)
        return None
