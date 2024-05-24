#!/usr/bin/env python3
'''
1. Simple pagination
'''
from typing import Tuple
import csv
import math
from typing import List


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
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        index_page, end_page = index_range(page, page_size)
        data = self.dataset()
        if index_page > len(data):
            return []
        return data[index_page:end_page]
