#!/usr/bin/python3
def add_tuple(tuple_a: tuple = (), tuple_b: tuple = ()):
    """ sum two tuples

        :tuple_a: first tuple
        :tuple_b: second tuple
    """
    def tuple_check(tuple_x):
        tuple_length = len(tuple_x)
        if tuple_length == 0:
            return (0, 0)
        if tuple_length == 1:
            return (tuple_x[0], 0)
        if tuple_length > 2:
            return (tuple_x[0], tuple_x[1])
        return tuple_x
    tuple_1 = tuple_check(tuple_a)
    tuple_2 = tuple_check(tuple_b)
    return (tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1])
