#!/usr/bin/python3
def print_list_integer(my_list:list=[]) -> None:
    """function that prints all integers of a list

    :my_list: integer list
    """
    for integer in my_list:
        print("{:d}".format(integer))
