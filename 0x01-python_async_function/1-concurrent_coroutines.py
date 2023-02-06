#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async.
"""
import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Takes in 2 int arguments (in this order): n and max_delay.
    You will spawn wait_random n times with the specified max_delay.
    :return: the list of all the delays (float values).
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
