#!/usr/bin/env python3
'''
Execute Multiple Coroutines at the same time
'''

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """
    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): max_delay between wait_random(s)
    Returns:
        (List): the list of all the delays in ascending order
    """
    res = [wait_random(max_delay) for _ in range(n)]
    return [await i for i in asyncio.as_completed(res)]
