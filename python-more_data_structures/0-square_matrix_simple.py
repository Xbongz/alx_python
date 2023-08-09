#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    my_matrix = []

    for row in matrix:
        my_row = []
        for col in row:
            my_row.append(col ** 2)
            
        my_matrix.append(my_row)
    return my_matrix

    new_matrix = square_matrix_simple()
    print(new_matrix)