#!/usr/bin/env python3
"""
Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    :param input_list: list of floats.
    :return: their sum as a float.
    """
    return float(sum(input_list))
