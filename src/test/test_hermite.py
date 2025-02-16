import main.hermite
import main.newton
import unittest


class Test_Hermite(unittest.TestCase):

    def test_E2E(self):

        x_values = [1.3, 1.6, 1.9]
        f_values = [0.6200860, 0.4554022, 0.2818186]
        d_values = [-0.5220232, -0.5698959, -0.5811571]
        x_value = 1.5

        matrix = main.hermite.seed_matrix(x_values, f_values, d_values)
        main.newton.fill_matrix(matrix)
        result = main.newton.calculate_f_value(matrix, x_value)

        self.assertAlmostEqual(result, 0.51182770)

        return None
