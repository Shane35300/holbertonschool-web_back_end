#!/usr/bin/python3
""" BasiCache """
BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache defines a simple caching system that inherits
    from BaseCaching """

    def __init__(self):
        """ Initialize """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item
    def get(self, key):
        """ return the value linked to key """
        if key is None:
            return None
        return self.cache_data.get(key)
