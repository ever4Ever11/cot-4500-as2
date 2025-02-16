import main.spline
import unittest


class Test_Spline(unittest.TestCase):

    def test_E2E(self):

        x_values = [1, 2, 3]
        f_values = [2, 3, 5]

        A_matrix = main.spline.construct_A_matrix(x_values)
        b_vector = main.spline.construct_b_vector(x_values, f_values)

        x_vector = main.spline.solve_x_vector(A_matrix, b_vector)

        result1 = x_vector[1]

        self.assertAlmostEqual(result1, 0.75)

        x_values = [0, 1, 2, 3]
        f_values = [1, 2, 4, 8]

        A_matrix = main.spline.construct_A_matrix(x_values)
        b_vector = main.spline.construct_b_vector(x_values, f_values)

        x_vector = main.spline.solve_x_vector(A_matrix, b_vector)

        result1 = x_vector[1]
        result2 = x_vector[2]

        self.assertAlmostEqual(result1, 0.4)
        self.assertAlmostEqual(result2, 1.4)

        x_values = [0, 1, 2, 3]
        f_values = [1, 2.718281828, 7.389056099, 20.08553692]

        A_matrix = main.spline.construct_A_matrix(x_values)
        b_vector = main.spline.construct_b_vector(x_values, f_values)

        x_vector = main.spline.solve_x_vector(A_matrix, b_vector)

        result1 = x_vector[1]
        result2 = x_vector[2]

        self.assertAlmostEqual(result1, 0.75685264)
        self.assertAlmostEqual(result2, 5.83006675)

        return None
