#!/usr/bin/env python3
"""
A FIFO caching system that discards the newest item in the cache when it
exceeds the maximum limit.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    FIFI CLASS that remove the first item that entered a cache
    """
    def __init__(self):
        """Initialize the cache system."""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        self.cache_data[key] = item
        self.last_key = key

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.last_key]
            print(f"DISCARD: {self.last_key}")

        if self.cache_data:
            self.last_key = list(self.cache_data.keys())[-1]
        else:
            self.last_key = None

    def get(self, key):
        """Retrieve an item from the cache by key."""
        return self.cache_data.get(key, None)
