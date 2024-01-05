#!/usr/bin/env python3
"""
This module presentes an async fonction wich is coroutine called
async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""


from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """The coroutine will collect 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random numbers."""
    random_numbers = [number async for number in async_generator()]
    return random_numbers[:10]
