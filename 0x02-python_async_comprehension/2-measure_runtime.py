#!/usr/bin/env python3
"""Parallel Comprehension"""
import asyncio
import time

async_com = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure runtime of paralell comprehension with Async Gather

    Arguments:
        None

    Returns:
        measure_runtime: type (float)
    """
    start_time: float = time.time()
    await asyncio.gather(async_com(), async_com(), async_com(), async_com())
    end_time: float = time.time()
    measure_runtime: float = end_time - start_time
    return measure_runtime
