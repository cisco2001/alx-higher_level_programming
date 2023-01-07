#!/usr/bin/python3
def element_at(my_list: list, idx: int):
    """ Given an index, retrieves an element from a list

        :my_list: list of integers
        :idx: index
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
