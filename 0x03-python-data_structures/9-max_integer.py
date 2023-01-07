#!/usr/bin/python3
def max_integer(my_list: list = []):
    """ Given a list, find the biggest integer

        :my_list: list of integers
    """
    if my_list:
        biggest_integer = my_list[0]
        for integer in my_list:
            if integer > biggest_integer:
                biggest_integer = integer
        return biggest_integer
    return None
