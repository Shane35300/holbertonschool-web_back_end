#!/usr/bin/env python3
"""
This module presente function named
index_range that takes two integer arguments page and page_size
"""


def index_range(page, page_size):
    """The function should return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return in a list
    for those particular pagination parameters"""
    start = 0 + (page - 1) * page_size
    end = page_size * page
    return (start, end)
