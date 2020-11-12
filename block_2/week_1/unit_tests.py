import unittest


def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    pass


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        data = ['string', 1.5]
        for x in data:
            with self.subTest(case=x):
                self.assertRaises(TypeError, factorize, x)

    def test_negative(self):
        data = [-1, -10, -100]
        for x in data:
            with self.subTest(case=x):
                self.assertRaises(ValueError, factorize, x)

    def test_zero_and_one_cases(self):
        data = [0, 1]
        for x in data:
            with self.subTest(case=x):
                self.assertEqual((x,), factorize(x))

    def test_simple_numbers(self):
        data = [3, 13, 29]
        for x in data:
            with self.subTest(case=x):
                self.assertEqual((x,), factorize(x))

    # 6 → (2, 3),   26 → (2, 13),   121 --> (11, 11)
    def test_two_simple_multipliers(self):
        data = [6, 26, 121]
        answer = [(2, 3), (2, 13), (11, 11)]
        for x, y in zip(data, answer):
            with self.subTest(case=x):
                self.assertEqual(y, factorize(x))

    # 1001 → (7, 11, 13) ,   9699690 → (2, 3, 5, 7, 11, 13, 17, 19)
    def test_many_multipliers(self):
        data = [1001, 9699690]
        answer = [(7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19)]
        for x, y in zip(data, answer):
            with self.subTest(case=x):
                self.assertEqual(y, factorize(x))
