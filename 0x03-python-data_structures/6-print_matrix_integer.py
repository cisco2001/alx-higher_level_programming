#!/usr/bin/python3
def print_matrix_integer(matrix: list = [[]]) -> None:
    """ function that prints a matrix of integers

        :matrix: a list containing lists of integers
    """
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end=" ")
        print()
