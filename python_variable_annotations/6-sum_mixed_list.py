#!/usr/bin/python3
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    sum = 0.0  # or sum = float(0)
    for elem in mxd_lst:
        sum += float(elem)
    return sum
