#https://github.com/marcusmendez-lab/lab11--MM---SB-
# Partner 1: Marcus Mendez
# Partner 2: Stefan Behrmann
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(0, 2), 2)
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(-1, 2), 1)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(0, 2), -2)
        self.assertEqual(subtract(-1, -2), 1)
        self.assertEqual(subtract(-1, 2), 1)
    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(5, 5), 25)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(5, 20), 4)
        self.assertEqual(divide(-2, 10), -5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(5, 25), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 5)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self):
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(16), 4)
        with self.assertRaises(ValueError):
            square_root(-4)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()