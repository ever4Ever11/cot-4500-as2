import main.newton
import unittest


class Test_Newton(unittest.TestCase):

    def test_E2E(self):

        x_values = [8.1, 8.3, 8.6, 8.7]
        f_values = [16.94410, 17.56492, 18.50515, 18.82091]
        x_value = 8.4

        matrix = main.newton.seed_matrix(x_values, f_values)
        main.newton.fill_matrix(matrix)
        result = main.newton.calculate_f_value(matrix, x_value)

        self.assertAlmostEqual(result, 17.87714249)

        return None
