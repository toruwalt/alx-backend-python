#!/usr/bin/env python3
"""Return an Async function from non-async function"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an Async function from non-async function

    Arguments:
        max_delay: Delay in secs (type int)

    Returns:
        Async object: (type _asyncio.Task)
    """
    x = asyncio.create_task(wait_random(max_delay))
    return x
