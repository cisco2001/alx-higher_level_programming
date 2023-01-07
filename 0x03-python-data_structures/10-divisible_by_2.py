#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """ Find all multiples of 2 in a list

        :my_list: a list
    """
    bool_list = []
    for integer in my_list:
        bool_list.append(bool(integer % 2))
    return bool_list
