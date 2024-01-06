#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for n in matrix:
            for r in n:
                print("{:d}".format(r), end=' 'if r != n[-1]else '')
            print()
