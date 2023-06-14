#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nmatrix = []
    for i in matrix:
        row = []
        for j in i:
            square = j**2
            row.append(square)
        nmatrix.append(row)
    return nmatrix
