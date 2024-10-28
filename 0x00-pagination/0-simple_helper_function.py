#!/usr/bin/env python
"""
A module that return a tuple of sixe 2, the start index
and the last index
"""


def index_range(page: int, page_size: int)-> tuple:
    """This function calculate the start and the end
    indexes for pagnation
    """
    start_index = (page - 1) * page_size

    end_index = start_index + page_size

    tuple_range = (start_index, end_index)

    return range tuple
