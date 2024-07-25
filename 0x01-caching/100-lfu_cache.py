#!/usr/bin/env python3
'''A basic dictionary LFU caching system'''

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    '''A class for implementing the dictionary methods of caching'''

    def __init__(self):
        '''An initialization method'''
        super().__init__()
        self.data = []
        self.frequency = {}

    def put(self, key, item):
        '''Puts cache data into the cache dictionary'''
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.data) >= BaseCaching.MAX_ITEMS:
                discard = sorted(
                    self.frequency.items(), key=lambda x: x[1])[0][0]
                del self.cache_data[discard]
                del self.frequency[discard]
                print(f"DISCARD: {discard}")
            self.frequency[key] = 1
            self.data.append(key)
        else:
            self.frequency[key] += 1
        self.cache_data[key] = item

    def get(self, key):
        '''Gets an item from the cache dictionary'''
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        return self.cache_data.get(key)
