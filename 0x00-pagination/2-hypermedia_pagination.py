#!/usr/bin/env python3
"""
2. Hypermedia pagination
"""
from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Function that takes two integer arguments and return a tuple of size two
    containing a start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters.
    '''
    return ((page - 1) * page_size, (page - 1) * page_size + page_size)


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
        '''
        Return the appropriate page of the dataset.
        '''
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        index_page, end_page = index_range(page, page_size)
        data = self.dataset()
        if index_page > len(data):
            return []
        return data[index_page:end_page]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''
        returns a dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        '''
        next_page = page + 1
        prev_page = page - 1
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        if next_page >= total_pages:
            next_page = None
        if prev_page <= 0:
            prev_page = None
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
