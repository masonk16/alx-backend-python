#!/usr/bin/env python3
"""
0. The basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument
    waits for a random delay between 0 and max_delay
    (included and float value) seconds.
    :param max_delay: int argument, with a default value of 10
    :return:
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
