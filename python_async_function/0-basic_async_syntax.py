#!/usr/bin/python3
"""
This module shows an asynchronous coroutine wait_random
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """takes in an integer argument named wait_random that waits for a random
    delay between 0 and max_delay seconds and eventually returns it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
