#!/usr/bin/env python3
'''A basic dictionary LIFO caching system'''

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''A class for implementing the dictionary methods of caching'''

    def __init__(self):
        '''An initialization method'''
        super().__init__()
        self.stack = []

    def put(self, key, item):
        '''Puts cache data into the cache dictionary'''
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.stack) >= BaseCaching.MAX_ITEMS:
                discard = self.stack.pop()
                del self.cache_data[discard]
                print(f"DISCARD: {discard}")
        else:
            self.stack.remove(key)
        self.stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        '''Gets an item from the cache dictionary'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
