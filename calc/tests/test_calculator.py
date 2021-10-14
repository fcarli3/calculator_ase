from calc.calculator import calculator as c
import unittest

# TODO: Extend these unit tests for the calculator module!


class TestAdd(unittest.TestCase):
    def test_add_integers_positive(self):
        result = c.sum(1, 2)
        self.assertEqual(result, 3)

    def test_add_integers_negative(self):
        result = c.sum(-1, -2)
        self.assertEqual(result, -3)

    def test_add_integers_pos_neg(self):
        result = c.sum(1, -2)
        self.assertEqual(result, -1)

    def test_add_integers_neg_pos(self):
        result = c.sum(-1, 2)
        self.assertEqual(result, 1)

    def test_divide_integers_positive(self):
        result = c.divide(6, 3)
        self.assertEqual(result, 2)

    def test_divide_integers_positive2(self):
        result = c.divide(7, 3)
        self.assertEqual(result, 2)

    def test_divide_integers_negative(self):
        result = c.divide(-6, -2)
        self.assertEqual(result, 3)

    def test_divide_integers_negative2(self):
        result = c.divide(-7, -2)
        self.assertEqual(result, 3)

    def test_divide_integers_pos_neg(self):
        result = c.divide(6, -2)
        self.assertEqual(result, -3)

    def test_divide_integers_pos_neg2(self):
        result = c.divide(9, -2)
        self.assertEqual(result, -4)

    def test_divide_integers_neg_pos(self):
        result = c.divide(-6, 2)
        self.assertEqual(result, -3)

    def test_divide_integers_neg_pos2(self):
        result = c.divide(-7, 2)
        self.assertEqual(result, -3)

    def test_divide_zero(self):
        result = c.divide(0, 2)
        self.assertEqual(result, 0)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, c.divide, 6, 0)

    def test_subtract_zero_from_one(self):
        result = c.subtract(1, 0)
        self.assertEqual(result, 1)

    def test_subtract_same_number(self):
        result = c.subtract(4, 4)
        self.assertEqual(result, 0)

    def test_subtract_from_zero(self):
        result = c.subtract(0, 5)
        self.assertEqual(result, -5)

    def test_subtract_just_one(self):
        result = c.subtract(5, 1)
        self.assertEqual(result, 4)

    def test_subtract_plus_one(self):
        result = c.subtract(5, -1)
        self.assertEqual(result, 6)

    def test_subtract_positive(self):
        result = c.subtract(1, 2)
        self.assertEqual(result, -1)

    def test_subtract_first_arg_negative(self):
        result = c.subtract(-1, 2)
        self.assertEqual(result, -3)

    def test_subtract_second_arg_negative(self):
        result = c.subtract(1, -2)
        self.assertEqual(result, 3)

    def test_subtract_both_non_positive(self):
        result = c.subtract(-1, -2)
        self.assertEqual(result, 1)

    def test_multiply_by_zero(self):
        result = c.multiply(0, 5)
        self.assertEqual(result, 0)

    def test_multiply_by_one(self):
        result = c.multiply(1, 5)
        self.assertEqual(result, 5)

    def test_multiply_by_negative_m(self):
        result = c.multiply(-2, 5)
        self.assertEqual(result, -10)

    def test_multiply_by_negative_m(self):
        result = c.multiply(2, -5)
        self.assertEqual(result, -10)

    def test_multiply_two_negative(self):
        result = c.multiply(-2, -5)
        self.assertEqual(result, 10)

    def test_multiply_negative_by_negative_zero(self):
        result = c.multiply(-0, -5)
        self.assertEqual(result, 0)

    def test_multiply_negative_by_positive_zero(self):
        result = c.multiply(0, -5)
        self.assertEqual(result, 0)

    def test_multiply_negative_by_negative_zero(self):
        result = c.multiply(-0, 5)
        self.assertEqual(result, 0)

    def test_multiply_negative_by_positive_zero(self):
        result = c.multiply(0, 5)
        self.assertEqual(result, 0)

    def test_multiply_first_case_positive(self):
        result = c.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_multiply_second_case_negative(self):
        result = c.multiply(2, -3)
        self.assertEqual(result, -6)

    def test_multiply_third_case_negative(self):
        result = c.multiply(-2, -3)
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()