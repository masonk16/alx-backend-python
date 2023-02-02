#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Type-annotated function to_kv
    :param k: string.
    :param v: int or float.
    :return: a tuple. First element of the tuple is the string k.
    The second element is the square of the int/float v
    and should be annotated as a float.
    """
    return (k, float(v**2))
