#!/usr/bin/env python3
"""List with type-annotation"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list input_list of floats as argument
    and returns their sum as a float.

    Argument:
        input_list: type of list

    Returns:
        list_sum: type of list
    """
    list_sum: float = 0
    for item in input_list:
        list_sum += item
    return list_sum
