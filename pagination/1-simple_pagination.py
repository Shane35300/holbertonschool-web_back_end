#!/usr/bin/env python3
"""
This module presente function named
index_range that takes two integer arguments page and page_size
"""

import csv
import math
from typing import List

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
