#!/usr/bin/python3
""" FIFOCache """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a simple caching system that inherits
    from BaseCaching """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.list = []

    def put(self, key, item):
        """ Add an item in the cache (FIFO) """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                key_to_remove = self.list.pop(0)
                del self.cache_data[key_to_remove]
                print(f"DISCARD: {key_to_remove}")
            self.cache_data[key] = item
            self.list.append(key)

    def get(self, key):
        """ return the value linked to key """
        if key is None:
            return None
        else:
            return self.cache_data.get(key)
