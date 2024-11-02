#!/usr/bin/env python3
"""
FIFI CLASS that remove the first item that entered a cache
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A FIFO caching system that discards the oldest item in the cache when it
    exceeds the maximum limit.
    """
    def __init__(self):
        """Initialize the cache system."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Retrieve an item from the cache by key."""
        return self.cache_data.get(key, None)
    