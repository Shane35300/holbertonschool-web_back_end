#!/usr/bin/env python3
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values)"""
    liste = []
    for x in range(n):
        liste.append(await wait_random(max_delay))  # Ajoutez chaque délai à la liste
    return sorted(liste)
