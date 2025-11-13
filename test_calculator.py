#https://github.com/Andres-Arvelo/lab11-AA-FZ.git
#Partner 1: Andres Arvelo
#Partner 2: Fareed Zaki

import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-10, 5), -5)

    def test_sub(self):
        self.assertEqual(calculator.sub(5,2),3)
        self.assertEqual(calculator.sub(5,-2),7)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0,10)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.log(2, 8), 3.0)


    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.log(0, 5)  #  base = 0
        with self.assertRaises(ValueError):
            calculator.log(1, 5)  #  base = 1
