#!/usr/bin/env python3
"""
this module create an async generator
"""


import random
import asyncio


async def async_generator():
    """ coroutine will loop 10 times, each time asynchronously
    wait 1 second, then yield a random number between 0 and 10"""
    for loop in range(10):
        nb = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield nb
