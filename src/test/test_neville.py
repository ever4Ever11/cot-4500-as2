import main.neville
import unittest


class Test_Neville(unittest.TestCase):

    def test_E2E(self):

        x_values = [2.0, 2.2, 2.3]
        f_values = [0.6931, 0.7885, 0.8329]
        x_value = 2.1

        result = main.neville.calculate_f_value(x_values, f_values, x_value)

        self.assertAlmostEqual(result, 0.74189999)

        x_values = [1.0, 1.3, 1.6, 1.9, 2.2]
        f_values = [0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623]
        x_value = 1.5

        result = main.neville.calculate_f_value(x_values, f_values, x_value)

        self.assertAlmostEqual(result, 0.51181999)

        return None
