import math


def calculate_f_value(x_values, f_values, x_value, *, tolerance=10**-5):

    length = len(x_values)

    intermediates = [f_values[0]] + [0] * (length-1)

    for ui in range(1, length):

        xupper = x_values[ui]

        pn = f_values[ui]

        for i, li in enumerate(range(ui-1, -1, -1)):

            xlower = x_values[li]

            pi = intermediates[i]
            intermediates[i] = pn

            pn = (x_value - xlower)*pn - (x_value - xupper)*pi
            pn /= xupper - xlower

        intermediates[ui] = pn

        d = intermediates[ui] - intermediates[ui-1]
        if math.fabs(d) < tolerance:
            break

    return intermediates[-1]
