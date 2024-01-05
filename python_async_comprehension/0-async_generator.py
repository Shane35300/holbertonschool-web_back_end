#!/usr/bin/env python3
"""
This module creates an asynchronous generator that
yields random floating-point numbers.coroutine called async_generator
that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that loops 10 times, with each iteration
    asynchronously
    waiting for 1 second and then yielding a random floating-point number
    between 0 and 10.

    Returns:
    AsyncGenerator[float, None]: An asynchronous generator
    yielding random floating-point numbers.
    """
    for loop in range(10):
        nb = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield nb
