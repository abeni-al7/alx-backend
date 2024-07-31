#!/usr/bin/env python3
'''A basic dictionary caching system'''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''A class for implementing the dictionary methods of caching'''

    def __init__(self):
        '''An initialization method'''
        super().__init__()

    def put(self, key, item):
        '''Puts cache data into the cache dictionary'''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''Gets an item from the cache dictionary'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
