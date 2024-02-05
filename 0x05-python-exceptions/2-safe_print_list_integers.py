#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    number_of_integers = 0
    while index < x:
        try:
            print("{:d}".format(my_list[index]), end="")
            number_of_integers += 1
        except (TypeError, ValueError):
            pass
        index += 1
    print()
    return number_of_integers
