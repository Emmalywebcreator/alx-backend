#!/usr/bin/python3
""" MRU Cache Module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache defines a caching system following the Most Recently Used (MRU)
    eviction policy.
    """

    def __init__(self):
        """
        Initialize the MRUCache by calling the parent class
        initializer and setting up an attribute to keep
        track of the most recently used key.
        """
        super().__init__()
        self.most_recently_used_key = None

    def put(self, key, item):
        """
        Add an item to the cache using the MRU policy.
       """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.most_recently_used_key = key

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.most_recently_used_key:
                print(f"DISCARD: {self.most_recently_used_key}")
                del self.cache_data[self.most_recently_used_key]

            self.most_recently_used_key = None

    def get(self, key):
        """
        Retrieve an item from the cache by its key.
        """
        if key in self.cache_data:
            self.most_recently_used_key = key
            return self.cache_data[key]
        return None
