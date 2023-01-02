#!/usr/bin/python3

def matrix_divided(matrix, div):
    """ A function that divides all the element of a matrix

    Args:
        matrix: List of List of integers or floats
        div: must be a number (integer or float
    Raises:
        TypeError: when matrix is neither a float an integer
        ZeroError: when div is equal zero
    Return:
        new matrix: matrix divided by div to 2 decimal places
    """
    new_matrix = []
    row_len = len(matrix[0])

    if not isinstance(div, (int,float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if row_len != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
        inner_list = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                new_ele = element / div
                inner_list.append(round(new_ele, 2))
        new_matrix.append(inner_list)

    return new_matrix
