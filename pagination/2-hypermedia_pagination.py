#!/usr/bin/env python3
"""
This module presente function named
index_range that takes two integer arguments page and page_size
"""

import csv
import math
from typing import List, Dict

index_range = __import__('0-simple_helper_function').index_range


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
        """
        takes two integer arguments page with default value 1 and
        page_size with default value 10
        """
        assert isinstance(page, int) and isinstance(page_size, int), """
        page and page_size should be integers"""
        assert page > 0 and page_size > 0, "value error"
        appropriate_page = index_range(page, page_size)
        liste = self.dataset()
        selection = []
        for elem in liste[appropriate_page[0]:appropriate_page[1]]:
            if elem:
                selection.append(elem)
        return selection

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """method that takes the same arguments (and defaults) as get_page
        and returns a dictionary containing the following key-value pairs:

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer"""
        entire_list = self.dataset()
        count = len(entire_list)
        if count % page_size == 0:
            total_page = count / page_size
        else:
            total_page = (count / page_size) + 1
        data = self.get_page(page, page_size)
        next_page = 0
        if page >= total_page or page < 1:
            next_page = None
            page_size = 0
        else:
            next_page = page + 1
        prev_page = 0
        if page <= 1:
            prev_page = None
        else:
            prev_page = page - 1
        dico = {'page_size': page_size, 'page': page, 'data': data,
                'next_page': next_page, 'prev_page': prev_page,
                'total_pages': int(total_page)
                }
        return dico
