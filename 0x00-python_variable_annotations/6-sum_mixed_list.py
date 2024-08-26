#!/usr/bin/env python3
"""Mixed List with Type-Annotation"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    takes a list mxd_lst of integers and floats
    and returns their sum as a float

    Arguments:
        mxd_lst: A list of integers and floats

    Returns:
        sum_list: A type of float
    """
    sum_list = 0
    for item in mxd_lst:
        sum_list += item
    return sum_list
