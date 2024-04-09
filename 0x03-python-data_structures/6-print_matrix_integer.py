#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        count = 0
        for x in row:
            count += 1
            print('{:d}'.format(x), end=(" " if count < len(row) else ""))
        print()
