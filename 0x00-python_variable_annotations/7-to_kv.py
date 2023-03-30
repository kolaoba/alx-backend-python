#!/usr/bin/env python3
"""
Type-annotated function to_kv that takes
    a string k and
    an int OR float v
as arguments and
returns a tuple
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """Returns a tuple of a string and a float

    Args:
        k (str): string element
        v (Union[int, float]): int or float element

    Returns:
        Tuple: tuple of arguments k and v
    """
    return (k, v**2)