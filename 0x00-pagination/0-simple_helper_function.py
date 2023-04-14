#!/usr/bin/env python3
"""helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two containing a start index and an end index"""
    start_index = (page - 1) * page_size
    end_page = page * page_size
    return start_index, end_page
