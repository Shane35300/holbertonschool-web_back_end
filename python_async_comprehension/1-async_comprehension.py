#!/usr/bin/python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension():
    liste = []
    async for x in async_generator():
        liste.append(x)
    return liste
