#!/usr/bin/python3
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string k and an int OR float v as arguments
    and returns a tuple"""
    if isinstance(v, int):
        square = v * v
    else:
        square = float(v) * float(v)
    return (k, square)
