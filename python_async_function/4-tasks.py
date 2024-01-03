#!/usr/bin/env python3
"""
This module shows an asynchronous coroutine task_wait_n
"""


from typing import List
import asyncio


task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values)"""
    liste = []
    for x in range(n):
        liste.append(await asyncio.create_task(task_wait_random(max_delay)))
    return sorted(liste)
