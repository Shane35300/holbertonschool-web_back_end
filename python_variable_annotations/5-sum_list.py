#!/usr/bin/env python3
"""
This module show a type-annotated function sum_list
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes a list input_list of floats
    as argument and returns their sum as a float"""
    sum = float(0)  # or sum = 0.0
    for elem in input_list:
        sum += float(elem)
    return sum
