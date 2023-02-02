#!/usr/bin/env python3
"""
Let's duck type an iterable object
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    :param lst: Iterable object.
    :return:  values with the appropriate types
    """
    return [(i, len(i)) for i in lst]