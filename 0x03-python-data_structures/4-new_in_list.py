#!/usr/bin/python3
def new_in_list(my_list: list, idx: int, element: int) -> list:
    """" replaces an element in a list without modifying the original list

         :my_list: list of values
         :idx: index
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
