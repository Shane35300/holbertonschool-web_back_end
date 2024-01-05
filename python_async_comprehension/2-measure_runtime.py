#!/usr/bin/env python3
"""
This module is an async function, it return the total runtime
"""


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """That measures the runtime:
    measure_runtime should measure the total runtime and return it
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*[async_comprehension() for x in range(4)])
    end_time = asyncio.get_event_loop().time()
    total_time = end_time - start_time
    return total_time
