#!/usr/bin/env python3
"""Async Comprehension"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Runs an Asynchronous Generator

    Yields:
        A value of type float
    """

    list = [item async for item in async_generator()]
    return list
