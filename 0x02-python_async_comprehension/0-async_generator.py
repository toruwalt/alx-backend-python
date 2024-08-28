#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Runs an Asynchronous Generator

    Yields:
        A value of type float
    """
    for i in range(10):
        await asyncio.sleep(1)
        x: float = random.uniform(0, 10)
        yield x
