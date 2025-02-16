import numpy


def construct_A_matrix(x_values):

    rows = columns = length = len(x_values)

    matrix = numpy.array([[0.0]*columns]*rows)
    matrix[0][0] = 1
    matrix[rows-1][columns-1] = 1

    for k in range(2, length):

        i = k-2
        j = row = k-1

        xi = x_values[i]
        xj = x_values[j]
        xk = x_values[k]

        hi = xj - xi
        hj = xk - xj

        matrix[row][i] = hi
        matrix[row][j] = 2 * (hi + hj)
        matrix[row][k] = hj

    return matrix


def construct_b_vector(x_values, f_values):

    length = len(x_values)

    vector = numpy.array([0.0]*length)
    vector[0] = 0
    vector[length-1] = 0

    for k in range(2, length):

        i = k-2
        j = row = k-1

        xi = x_values[i]
        xj = x_values[j]
        xk = x_values[k]

        ai = f_values[i]
        aj = f_values[j]
        ak = f_values[k]

        hi = xj - xi
        hj = xk - xj

        vector[row] = 3 * ((ak-aj)/hj - (aj-ai)/hi)

    return vector


def solve_x_vector(A_matrix, b_vector):
    return numpy.linalg.solve(A_matrix, b_vector)
