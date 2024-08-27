#!/usr/bin/env python3
"""Async in a loop"""

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Runs an asynchronous loop within a function

    Arguments:
        n: Number of times to run loop (type int)
        max_delay: Delay in secs (type int)

    Returns:
        list_delay: A list of delays (type float)
    """
    list_delay = [await wait_random(max_delay) for x in range(0, n)]
    list_delay.sort()
    return list_delay
