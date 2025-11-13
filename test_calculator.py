import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(-4, 5), -20)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(7, 2), 3.5)
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(10, -5)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(0, 0), 0)
        self.assertEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(25), 5)

