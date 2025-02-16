import numpy


def seed_matrix(x_values, f_values):

    length = len(x_values)

    rows = length
    columns = length + 1
    matrix = numpy.array([[0.0]*columns]*rows)

    for i, (xv, fv) in enumerate(zip(x_values, f_values)):

        matrix[i][0] = xv
        matrix[i][1] = fv

    return matrix


def fill_matrix(matrix):

    rows, columns = matrix.shape

    for i, r in enumerate(range(1, rows), start=3):

        if i > columns:
            i = columns

        for c in range(2, i):

            if matrix[r][c] != 0.0:
                continue

            pv1 = matrix[r][c-1]
            pv0 = matrix[r-1][c-1]
            xv1 = matrix[r][0]
            xv0 = matrix[r-c+1][0] # (r-1)-(c-2)

            matrix[r][c] = (pv1 - pv0) / (xv1 - xv0)

    return None


def coefficients(matrix):

    rows, columns = matrix.shape

    coefficients = []
    for r in range(min(rows, columns-1)):
        coefficients.append(matrix[r][r+1])

    return coefficients


def calculate_f_value(matrix, x_value):

    rows, columns = matrix.shape

    acc = 1
    f_value = matrix[0][1]

    for r in range(1, min(rows, columns-1)):

        acc *= x_value - matrix[r-1][0]
        f_value += matrix[r][r+1] * acc

    return f_value
