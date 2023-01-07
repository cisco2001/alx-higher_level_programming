#!/usr/bin/python3
def print_reversed_list_integer(my_list: list = []) -> None:
    """ a function that prints all integers of a list, in reverse order

        :my_list: list of integers
    """
    my_list.reverse()
    for integer in my_list:
        print("{:d}".format(integer))
