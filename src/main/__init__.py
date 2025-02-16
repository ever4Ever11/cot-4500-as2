class UnbalancedDataError(Exception):
    """Raised when the data provided is unbalanced"""

    def __init__(self, name1, name2):
        self.message = f'unbalanced data sets {name1} and {name2}'
        return None

    def __str__(self):
        return self.message


class InsufficientDataError(Exception):
    """Raised when the data provided is insufficient"""

    def __init__(self, length):
        self.message = f'insufficient data set length {length}'
        return None

    def __str__(self):
        return self.message


class IntervalError(Exception):
    """Raised when given value does not fall within given range"""

    def __init__(self, v, minv, maxv):
        self.message = f'value {v} not contained within range {minv} - {maxv}'

    def __str__(self):
        return self.message


def check_balance(name1, values1, name2, values2):

    if len(values1) != len(values2):
        raise UnbalancedDataError(name1, name2)

    return None


def check_length2(values):

    if len(values) < 2:
        raise InsufficientDataError(len(values))

    return None


def check_length3(values):

    if len(values) < 3:
        raise InsufficientDataError(len(values))

    return None


def check_containment(value, values):

    min_value = min(values)
    max_value = max(values)
    if value < min_value or max_value < value:
        raise IntervalError(value, min_value, max_value)

    return None
