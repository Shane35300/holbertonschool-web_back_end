#!/usr/bin/env python3
"""
This module show a type-annotated function sum_mixed_list
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a list mxd_lst of integers and floats and returns
    their sum as a float"""

    sum = 0.0  # or sum = float(0)
    for elem in mxd_lst:
        sum += float(elem)
    return sum
