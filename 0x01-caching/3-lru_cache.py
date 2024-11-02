#!/usr/bin/env python3
""" LRU Cache Module """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache defines a caching system following the Least Recently Used (LRU)
    eviction policy..
    """

    def __init__(self):
        """
        Initialize the LRUCache by calling the parent class initializer
        and setting up an attribute to track the access order of cache keys.
        """
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """
        Add an item to the cache using the LRU policy.
        """
        if key is None or item is None:
            return

        # Update the cache with the new key-value pair
        if key in self.cache_data:
            # Remove the key from the access order if it exists
            self.access_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Evict the least recently used item
            least_recently_used = self.access_order.pop(0)
            print(f"DISCARD: {least_recently_used}")
            del self.cache_data[least_recently_used]

        self.cache_data[key] = item
        self.access_order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache by its key.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the key's position in the access order
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]
