#!/usr/bin/env python3
"""
This module creates an asynchronous generator that
yields random floating-point numbers.
"""


from typing import AsyncGenerator
import random
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that loops 10 times, with each iteration asynchronously
    waiting for 1 second and then yielding a random floating-point number between 0 and 10.

    Returns:
    AsyncGenerator[float, None]: An asynchronous generator yielding random floating-point numbers.
    """
    for loop in range(10):
        nb = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield nb
