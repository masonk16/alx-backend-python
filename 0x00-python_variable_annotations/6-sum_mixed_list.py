#!/usr/bin/env python3
"""
Complex types - mixed list.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Type-annotated function sum_mixed_list.
    :param mxd_lst: list of integers and floats.
    :return: their sum as a float.
    """
    return float(sum(mxd_lst))
