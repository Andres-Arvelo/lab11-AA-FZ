#https://github.com/Andres-Arvelo/lab11-AA-FZ.git
#Partner 1: Andres Arvelo
#Partner 2: Fareed Zaki

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-10, 5), -5)

    def test_sub(self):
        self.assertEqual(calculator.sub(5,2),3)
        self.assertEqual(calculator.sub(5,-2),7)
    def test_multiply(self):
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(-4, 5), -20)
        self.assertEqual(mul(0, 100), 0)

    def test_divide_by_zero(self):
    def test_divide(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(7, 2), 3.5)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0,10)
            div(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.log(2, 8), 3.0)

    def test_log_invalid_base(self):
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.log(0, 5)  #  base = 0
            log(10, -5)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(0, 0), 0)
        self.assertEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            calculator.log(1, 5)  #  base = 1
            square_root(-9)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(25), 5)

