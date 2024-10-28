#!/usr/bin/env python3
"""
A module that return a tuple of sixe 2, the start index
and the last indexi
"""


def index_range(page: int, page_size: int) -> tuple:
    """This function calculate the start and the end
    indexes for pagnation
    """
    start_index = (page - 1) * page_size

    end_index = page * page_size

    tuple_range = (start_index, end_index)

    return range_tuple
