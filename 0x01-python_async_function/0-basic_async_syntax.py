#!/usr/bin/env python3
"""Write an asynchronous coroutine with Type-Annotation"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asychronous Coroutine with delay

    Arguments:
        max-delay: type(int)

    Returns:
        task_delay: type(float)
    """
    task_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(task_delay)
    return task_delay
