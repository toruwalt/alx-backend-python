#!/usr/bin/env python3
"""Async in a loop"""

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    list_delay = [await wait_random(max_delay) for x in range(0, n)]
    list_delay.sort()
    return list_delay
