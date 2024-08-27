#!/usr/bin/env python3
"""Measure Asynchronous Task time"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Checks the total execution time per times spawned

    Arguments:
        n: Number of times to run loop (type int)
        max_delay: Delay in secs (type int)

    Returns:
        exec_time_per_spawn: (type float)
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return ((end_time - start_time) / n)
