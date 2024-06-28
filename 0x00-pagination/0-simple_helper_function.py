#!/usr/bin/env python3
"""Simple helper function for
the pagination project
"""


def index_range(page, page_size):
    """Calculate the range of content to
    send based on page number and
    page size"""
    start_point = (page - 1) * page_size
    end_point = page * page_size

    return (start_point, end_point)
