#!/usr/bin/env python3
"""
This module presentes an async fonction
"""


from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List:
    """The coroutine will collect 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random numbers."""
    liste = []
    async for x in async_generator():
        liste.append(x)
    return liste
