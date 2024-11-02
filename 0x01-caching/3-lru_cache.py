#!/usr/bin/env python3
""" LRU Cache Module """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache defines a caching system following the Least Recently Used (LRU)
    eviction policy. When the cache exceeds its limit, it discards the least
    recently accessed item to make space for new entries.
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

        Args:
            key (str): The key associated with the item to be added.
            item (Any): The item to be stored in the cache.

        If either `key` or `item` is None, this method does nothing. If the
        cache exceeds its maximum limit, the least recently used item is
        discarded and a message is printed with the discarded key.
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

        Args:
            key (str): The key associated with the item to be retrieved.

        Returns:
            The item associated with the key if it exists in the cache,
            or None if the key is not found or is None.

        Accessing an item updates its position in the access order list to
        reflect its recent use.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the key's position in the access order
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]

