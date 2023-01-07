#!/usr/bin/python3
def replace_in_list(my_list: list, idx: int, element):
    """ a function that replaces an element of a list at a specific position

        :my_list: a list
        :idx: specific position to replace element
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
