import numpy


def seed_matrix(x_values, f_values, d_values):

    length = len(x_values)

    rows = 2 * length
    columns = 2 * length + 1
    matrix = numpy.array([[0.0]*columns]*rows)

    for i, (xv, fv, dv) in enumerate(zip(x_values, f_values, d_values)):

        matrix[2*i][0] = xv
        matrix[2*i+1][0] = xv

        matrix[2*i][1] = fv
        matrix[2*i+1][1] = fv

        matrix[2*i+1][2] = dv

    return matrix
