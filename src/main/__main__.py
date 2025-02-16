import argparse
import logging
import main
import main.hermite
import main.neville
import main.newton
import main.spline
import numpy
import sys


def add_tolerance_option(parser):
    parser.add_argument('-t', '--tolerance',
                        default=10**-5,
                        type=float,
                        help='halting tolerance of the calculation')
    return None


def add_x_values_required_option(parser):
    parser.add_argument('--x-values',
                        nargs='+',
                        type=float,
                        required=True,
                        help='x-values data, length must equal f-value')
    return None


def add_f_values_required_option(parser):
    parser.add_argument('--f-values',
                        nargs='+',
                        type=float,
                        required=True,
                        help='f-values data, length must equal x-values')
    return None


def add_d_values_required_option(parser):
    parser.add_argument('--d-values',
                        nargs='+',
                        type=float,
                        required=True,
                        help='d-values data, length must equal x-values')
    return None


def add_x_value_required_option(parser):
    parser.add_argument('--x-value',
                        type=float,
                        required=True,
                        help='x to be approximated, must be within x-values')
    return None


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--steps',
                    action='store_true',
                    help='shows the steps of the calculation')
subparsers = parser.add_subparsers(dest='command',
                                   required=True,
                                   help='selects the numerical method')


subparsers.add_parser('answers',
                      help='provides the answers to the questions')


subparser = subparsers.add_parser('neville',
                                  help='approximates a given x value')
add_tolerance_option(subparser)
add_x_values_required_option(subparser)
add_f_values_required_option(subparser)
add_x_value_required_option(subparser)


subparser = subparsers.add_parser('newton',
                                  help='approximates a given x value')
add_x_values_required_option(subparser)
add_f_values_required_option(subparser)
add_x_value_required_option(subparser)


subparser = subparsers.add_parser('hermite',
                                  help='approximates a given x value')
add_x_values_required_option(subparser)
add_f_values_required_option(subparser)
add_d_values_required_option(subparser)
add_x_value_required_option(subparser)


subparser = subparsers.add_parser('spline',
                                  help='constructs the matrix and vectors')
add_x_values_required_option(subparser)
add_f_values_required_option(subparser)


args = parser.parse_args()


logger = logging.getLogger()
logger.setLevel(logging.DEBUG if args.steps else logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))


try:

    if args.command == 'answers':

        # Question 1.

        x_values = [3.6, 3.8, 3.9]
        f_values = [1.675, 1.436, 1.318]
        x_value = 3.7

        f_value = main.neville.calculate_f_value(x_values, f_values, x_value)

        logger.info(f'{f_value}\n')

        # Question 2.

        x_values = [7.2, 7.4, 7.5, 7.6]
        f_values = [23.5492, 25.3913, 26.8224, 27.4589]

        matrix = main.newton.seed_matrix(x_values, f_values)
        logger.debug(f'Seed: {matrix}')

        main.newton.fill_matrix(matrix)
        logger.debug(f'Fill: {matrix}')

        coefficients = main.newton.coefficients(matrix)

        logger.info(coefficients[1])
        logger.info(coefficients[2])
        logger.info(f'{coefficients[3]}\n')

        # Question 3.

        x_value = 7.3

        f_value = main.newton.calculate_f_value(matrix, x_value)

        logger.info(f'{f_value}\n')

        # Question 4.

        x_values = [3.6, 3.8, 3.9]
        f_values = [1.675, 1.436, 1.318]
        d_values = [-1.195, -1.188, -1.182]

        matrix = main.hermite.seed_matrix(x_values,
                                          f_values,
                                          d_values)
        logger.debug(f'Seed: {matrix}')

        main.newton.fill_matrix(matrix)

        logger.info(f'{matrix}\n')

        # Question 5.

        x_values = [2, 5, 8, 10]
        f_values = [3, 5, 7, 9]

        A_matrix = main.spline.construct_A_matrix(x_values)

        logger.info(A_matrix)

        b_vector = main.spline.construct_b_vector(x_values,
                                                  f_values)

        logger.info(b_vector)

        x_vector = main.spline.solve_x_vector(A_matrix, b_vector)

        logger.info(x_vector)

    elif args.command == 'neville':

        main.check_balance('x_values', args.x_values,
                           'f_values', args.f_values)
        main.check_length2(args.x_values)
        main.check_containment(args.x_value, args.x_values)

        f_value = main.neville.calculate_f_value(args.x_values,
                                                 args.f_values,
                                                 args.x_value,
                                                 tolerance=args.tolerance)

        logger.info(f_value)

    elif args.command == 'newton':

        main.check_balance('x_values', args.x_values,
                           'f_values', args.f_values)
        main.check_length2(args.x_values)
        main.check_containment(args.x_value, args.x_values)

        matrix = main.newton.seed_matrix(args.x_values, args.f_values)
        logger.debug(f'Seed: {matrix}')

        main.newton.fill_matrix(matrix)
        logger.debug(f'Fill: {matrix}')

        f_value = main.newton.calculate_f_value(matrix, args.x_value)

        logger.info(f_value)

    elif args.command == 'hermite':

        main.check_balance('x_values', args.x_values,
                           'f_values', args.f_values)
        main.check_balance('x_values', args.x_values,
                           'd_values', args.d_values)
        main.check_length2(args.x_values)
        main.check_containment(args.x_value, args.x_values)

        matrix = main.hermite.seed_matrix(args.x_values,
                                          args.f_values,
                                          args.d_values)
        logger.debug(f'Seed: {matrix}')

        main.newton.fill_matrix(matrix)
        logger.debug(f'Fill: {matrix}')

        f_value = main.newton.calculate_f_value(matrix, args.x_value)

        logger.info(f_value)

    elif args.command == 'spline':

        main.check_balance('x_values', args.x_values,
                           'f_values', args.f_values)
        main.check_length3(args.x_values)

        A_matrix = main.spline.construct_A_matrix(args.x_values)

        logger.info(A_matrix)

        b_vector = main.spline.construct_b_vector(args.x_values,
                                                  args.f_values)

        logger.info(b_vector)

        x_vector = main.spline.solve_x_vector(A_matrix, b_vector)

        logger.info(x_vector)

except ZeroDivisionError as e:
    logger.info(e)
except main.UnbalancedDataError as e:
    logger.info(e)
except main.InsufficientDataError as e:
    logger.info(e)
except main.IntervalError as e:
    logger.info(e)
except OverflowError:
    logger.info('calculation likely diverged')
except numpy.linalg.LinAlgError as e:
    logger.info(e)
except Exception:
    logger.info('unknown error, check your inputs are appropriate')
