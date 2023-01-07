#!/usr/bin/python3
def delete_at(my_list: list = [], idx: int = 0):
    """ Remove the item at a specific position in a list

        :my_list: a list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
