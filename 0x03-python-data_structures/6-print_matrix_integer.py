#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx in range(0, len(row)):
            if idx != len(row) - 1:
                print("{} ".format(row[idx]), end="")
            else:
                print("{}".format(row[idx]))
