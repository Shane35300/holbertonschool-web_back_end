#!/usr/bin/env python3
"""
this module create an async generator
"""


from typing import AsyncGenerator
import random
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """ coroutine will loop 10 times, each time asynchronously
    wait 1 second, then yield a random number between 0 and 10"""
    for loop in range(10):
        nb = random.uniform(0, 10)
        yield nb
        await asyncio.sleep(1)

