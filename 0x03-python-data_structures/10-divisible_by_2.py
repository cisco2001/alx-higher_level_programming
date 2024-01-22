#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    is_divisible = []
    for number in my_list:
        is_divisible.append(number % 2 == 0)
    return is_divisible
