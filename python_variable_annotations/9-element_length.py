#!/usr/bin/env python3
"""
This module show a type-annotated function element_length
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return the lenght of an element"""

    return [(i, len(i)) for i in lst]
