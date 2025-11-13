#https://github.com/Andres-Arvelo/lab11-AA-FZ.git
#Partner 1: Andres Arvelo
#Partner 2: Fareed Zaki

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    #Partner 2
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-10, 5), -5)
        self.assertEqual(add(4, 12), 16)

    def test_subtract(self):
        self.assertEqual(subtract(5,2),3)
        self.assertEqual(subtract(5,-2),7)
        self.assertEqual(subtract(10, 8), 2)

    #Parter 1
    def test_multiply(self):
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(-4, 5), -20)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(7, 2), 3.5)
        self.assertEqual(div(4, 2), 2)

    #Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 100.0), 2)
        self.assertAlmostEqual(logarithm(2, 8.0), 3)
        self.assertAlmostEqual(logarithm(3, 9.0), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)  # base = 0
        with self.assertRaises(ValueError):
            logarithm(1, 5)  # base = 1

    #Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(10,0)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(0, 0), 0)
        self.assertEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(25), 5)


#Do not touch this
if __name__ == "__main__":
    unittest.main()