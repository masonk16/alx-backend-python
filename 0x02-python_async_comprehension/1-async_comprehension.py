#!/usr/bin/env python3
"""
Async Random Number Comprehensions.
"""
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehensing
    over async_generator.
    :return: List of the 10 random numbers.
    """
    return [num async for num in async_generator()]
