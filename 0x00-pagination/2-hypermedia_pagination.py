#!/usr/bin/env python3
'''A module for implementing a simple pagination logic'''
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Returns the range of values of a list for a pagination'''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Returns a paginated list of items'''
        assert(type(page) == int and type(page_size) == int)
        assert(page > 0 and page_size > 0)
        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if end_index < len(data):
            return self.dataset()[start_index:end_index]
        else:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        '''Returns a hypermedia of the paginated data'''
        data = self.get_page(page, page_size)
        total_pages = math.floor(len(self.dataset()) / page_size)
        next_page = page + 1 if page + 1 < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
