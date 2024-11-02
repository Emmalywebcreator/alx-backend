#!/usr/bin/env python3
""""
A caching system that discards the least frequently used item when the
cache exceeds the limit. If items have the same frequency, it discards
the least recently used item among
"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    List frequently used
    """

    def __init__(self):
        """Initialize the cache system and additional tracking structures."""
        super().__init__()
        self.frequency = defaultdict(int)
        self.recency = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache, and apply LFU + LRU replacement policy
        when limit exceeded.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_frequency_and_recency(key)
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self._discard_lfu_item()

        self.cache_data[key] = item
        self.frequency[key] = 1
        self._update_recency(key)

    def get(self, key):
        """
        Retrieve an item from the cache by key, updating frequency
        and recency.
        """
        if key is None or key not in self.cache_data:
            return None
        self._update_frequency_and_recency(key)
        return self.cache_data[key]

    def _update_frequency_and_recency(self, key):
        """Update the access frequency and recency of a key."""
        self.frequency[key] += 1
        self._update_recency(key)

    def _update_recency(self, key):
        """Update the recency (LRU) order for the given key."""
        if key in self.recency:
            self.recency.pop(key)
        self.recency[key] = True

    def _discard_lfu_item(self):
        """
        Remove the least frequently used (and least recently used in case
        of tie) item.
        """
        min_freq = min(self.frequency.values())

        lfu_keys = [
            k for k, freq in self.frequency.items() if freq == min_freq
        ]

        if len(lfu_keys) > 1:
            oldest_lfu_key = next(k for k in self.recency if k in lfu_keys)
        else:
            oldest_lfu_key = lfu_keys[0]

        del self.cache_data[oldest_lfu_key]
        del self.frequency[oldest_lfu_key]
        self.recency.pop(oldest_lfu_key)

        print(f"DISCARD: {oldest_lfu_key}")
