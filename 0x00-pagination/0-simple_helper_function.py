#!/usr/bin/env python3
'''A module for finding the range of indexes for a given page and page size'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Returns the range of values of a list for a pagination'''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
